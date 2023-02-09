// SPDX-License-Identifier: MIT
pragma solidity 0.8.17;


contract PriceConsumer {
    uint256 priceFeed;
    constructor() {
        priceFeed = block.timestamp;
    }
     function setLatestPrice() public{
         priceFeed = block.timestamp;
     }
    /**
     * Returns the latest price.
     */
    function getPrice() public view returns (uint256) {
        uint256 price = (priceFeed * 7) * 1000000000;
        return price;
    }
    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }
}
