#!/usr/bin/env python
from brownie import accounts, Lottery, network, config, MockV3Aggregator  # type: ignore
from web3 import Web3

def deploys(force=False):
    account = accounts[0]
    if not len(MockV3Aggregator) or force:
        pricefeedAddress = MockV3Aggregator.deploy(
            8, Web3.toWei(2000, "ether"), {"from": account})
    if not len(Lottery) or force:
        Lottery.deploy(MockV3Aggregator[-1], {"from": account})

def main():
    deploys()
    print("network: ", network.show_active())
    account = accounts[0]
    lottery = Lottery[-1]
    print("enterance Fee: ",lottery.getEntranceFee())
    assert lottery.getEntranceFee() == 2500000
    print("Lottery state: ",lottery.lottery_state)
    assert lottery.lottery_state() == 0
    print("Players: ",lottery.players)
    assert len(lottery.players()) == 0
    print("Players: ",lottery.players)

def test_lottery():
    main()