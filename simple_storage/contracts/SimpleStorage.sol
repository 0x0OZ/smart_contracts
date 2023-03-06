// SPDX-License-Identifier: MIT
pragma solidity 0.8.17;

contract SimpleStorage{
    struct People{
        string name;
        uint256 balance;
    }
    People[] public people;
    function addPerson(string memory _name,uint256 _balance) public{
        people.push(People(_name,_balance));
    }


    uint256 favNum;
    constructor(){
        favNum = 777;
    }
function store(uint256 _favNum) public{
    favNum = _favNum;
}
function get() public view returns (uint256){
    return favNum;
}
}
