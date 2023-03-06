// SPDX-License-Identifier: MIT
pragma solidity 0.8.17;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@OpenZeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/mocks/VRFCoordinatorMock.sol";

contract Lottery is Ownable {
    address payable[] public players;
    address payable recentWinner;
    AggregatorV3Interface priceFeedAddress;
    uint256 usdEntryFee;
    enum LOTTERY_STATE {
        CLOSED,
        OPEN,
        CALCULATING_WINNERS
    }
    LOTTERY_STATE public lottery_state;
    event requestedRandomness(uint256 requestId);
    event chosenWinner(address winner);
    event soraka(uint256);

    constructor(address _pricefeedAddress) {
        //owner = msg.sender;
        usdEntryFee = 50 * (10**18);
        lottery_state = LOTTERY_STATE.CLOSED;
        priceFeedAddress = AggregatorV3Interface(_pricefeedAddress);
    }

    function runEvent(uint256 n) public {
        emit soraka(n);
    }

    function getPlayersCount() public view returns (uint256) {
        return players.length;
    }

    function enter() public payable {
        // requirement: $50 usd | maybe restrict how many times a person can join ?
        require(msg.value >= getEntranceFee(), "Need More ETH!");
        require(
            lottery_state == LOTTERY_STATE.OPEN,
            "lottery currently closed!"
        );
        players.push(payable(msg.sender));
    }

    function getEntranceFee() public view returns (uint256) {
        (, int256 _price, , , ) = priceFeedAddress.latestRoundData();
        uint256 price = uint256(_price) * (10**10); // 18 decimals
        // the calc that idk it
        // man damn it - why additional 10**18?? --
        //uint256 cost = (usdEntryFee * 10**18) / price;
        // I removed the 10**18 because it makes to sense
        uint256 cost = (usdEntryFee * (10**18)) / price;
        return cost;
    }

    function startLottery() public onlyOwner {
        require(
            lottery_state == LOTTERY_STATE.CLOSED,
            "You Can't start Lottery Yet!"
        );
        lottery_state = LOTTERY_STATE.OPEN;
    }

    function endLottery() public onlyOwner returns (uint256) {
        require(lottery_state == LOTTERY_STATE.OPEN, "You can't YET!");
        lottery_state = LOTTERY_STATE.CALCULATING_WINNERS;
        uint256 winner = fullfillRandomness(); // just a simulate - Don't use in REAL contract
        emit requestedRandomness(winner);
        // require(winner > 0, "random not found");
        recentWinner = players[winner];
        recentWinner.transfer(address(this).balance);
        emit chosenWinner(recentWinner);
        lottery_state = LOTTERY_STATE.CLOSED;
        return winner;
    }

    function fullfillRandomness() public view returns (uint256) {
        uint256 random = uint256(
            keccak256(
                abi.encodePacked(
                    msg.sender, // PREDICTABLE
                    block.timestamp, // PREDICTABLE
                    block.difficulty, // PREDICTABLE - can be manipulated by miners
                    block.gaslimit, // PREDICTABLE
                    block.coinbase, // PREDICTABLE
                    block.number, // PREDICTABLE
                    gasleft(), // IDK
                    msg.data //  controlled by user
                )
            )
        ) % players.length;

        return random;
    }
}
