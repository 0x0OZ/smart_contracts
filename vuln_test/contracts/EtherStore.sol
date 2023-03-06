// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract EtherStore {

    uint256 public withdrawalLimit = 1 ether;
    mapping(address => uint256) public lastWithdrawTime;
    mapping(address => uint256) public balances;

    function depositFunds() external payable {
        balances[msg.sender] += msg.value;
    }
    
    function withdrawFunds (uint256 _weiToWithdraw) public returns(bytes memory) {
        require(balances[msg.sender] >= _weiToWithdraw,"No ENough ETH!");
        // limit the withdrawal
        require(_weiToWithdraw <= withdrawalLimit,"EXCEED ETH LIMIT!");
        // limit the time allowed to withdraw
        //require(block.timestamp >= lastWithdrawTime[msg.sender] + 1 weeks);
        (bool test,bytes memory x) = msg.sender.call{value:_weiToWithdraw}("");
        balances[msg.sender] -= _weiToWithdraw;
        lastWithdrawTime[msg.sender] = block.timestamp;
        return x;
    }
 }