// contracts/soraka.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Soraka is ERC20 {
    event start(address indexed _owner,uint256 number);
    constructor(uint256 initialSupply) ERC20("Soraka", "SOR") {
        emit start(msg.sender,initialSupply);
        _mint(msg.sender, initialSupply);
    
    }
}

