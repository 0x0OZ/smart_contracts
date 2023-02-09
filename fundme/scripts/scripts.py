#!/usr/bin/env python
from brownie import accounts,network,config,MockV3Aggregator # type: ignore
from web3 import Web3

DECIMALS = 18
STARTING_PRICE = 200000000000
LOCAL_NETWORKS = ["development","ganache-local"]
def get_account():
    if network.show_active() in LOCAL_NETWORKS:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])
def get_mock():
    if network.show_active() not in LOCAL_NETWORKS:
        price_feed_address = config['networks'][network.show_active(
        )]['eth_usd_price_feed']
    else:
        if len(MockV3Aggregator) < 1:
            print("deploying Mock...")
            MockV3Aggregator.deploy(DECIMALS, Web3.toWei(
                STARTING_PRICE, "ether"), {"from": get_account()})
        price_feed_address = MockV3Aggregator[-1].address
        print(f"deployed mock: {price_feed_address}")
    return price_feed_address