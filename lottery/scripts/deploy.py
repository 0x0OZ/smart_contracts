#!/usr/bin/env python
from brownie import accounts, Lottery, network, config, MockV3Aggregator, VRFCoordinatorMock  # type: ignore
from web3 import Web3
import time
def get_account():
    # maybe add network things later
    return accounts[0]
def deploys():
    account = get_account()
    MockV3Aggregator.deploy(
        8, Web3.toWei(2000, "ether"), {"from": account})
    Lottery.deploy(
        MockV3Aggregator[-1], {"from": account})
    
def join_lottery():
    lottery = Lottery[-1]
    entrance_fee = lottery.getEntranceFee()
    for i in accounts:
        lottery.enter({"from": i, "value": entrance_fee})
def start_lottery():
    Lottery[-1].startLottery({"from":get_account()})
def end_lottery():
    return Lottery[-1].endLottery({"from":get_account()})
def main():
    print("network: ", network.show_active())
    deploys()
    account = accounts[0]
    lottery = Lottery[-1]
    print("state:", lottery.lottery_state())
    lottery.startLottery({"from":account})
    entrance_fee = lottery.getEntranceFee()
    print("entrance Fee: ", entrance_fee)
    join_lottery()
    print("Players: ",lottery.getPlayersCount())
    print("Lottery ETH :",lottery.balance())
    winner = end_lottery()
    print("lottery Over!")
    print("Winner : ",winner)
    print("state:", lottery.lottery_state())
