#!/usr/bin/env python
from brownie import accounts,network,config # type: ignore
from web3 import Web3

DECIMALS = 18
STARTING_PRICE = 200000000000
LOCAL_NETWORKS = ["development","ganache-local"]
def get_account():
    if network.show_active() in LOCAL_NETWORKS:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from'])

