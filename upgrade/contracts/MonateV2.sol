// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract MonateV2{
    uint256 private state;
    function modifyState(uint256 _state) public {
        state = _state;
    }
    function getState() public view returns(uint256){
        return state;
    }
    function increment() public{
        state += 1;
    }
}
