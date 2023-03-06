#!/usr/bin/env python
from brownie import accounts,config,network,Soraka # type: ignore
from scripts.scripts import get_account
from web3 import Web3
def main():
    account = get_account()
    amount = Web3.toWei("10","ether")
    #sora = Soraka.deploy(amount,{"from":account})
    sora = Soraka[-1]
    print("my addr: ",account)
    print(network.show_active())
    print(sora.balanceOf(account))
    to = accounts.add(config["wallets"]["from"])
    sora.approve(account,1000,{"from":account})
    sora.transferFrom(account,to,100,{"from":account})
    print(sora.balanceOf(account))