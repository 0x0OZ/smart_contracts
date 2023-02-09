#!/usr/bin/env python
from brownie import accounts, FundMe, network, config, MockV3Aggregator  # type: ignore
from scripts.scripts import get_account, get_mock

account = get_account()
try:
    fund_me = FundMe[-1]
except:
    pass

def fund(entrance_fee,account=account, fund_me=fund_me):
    fund_me.fund({"from": account, "value": entrance_fee})
def withdraw(account=account):
    fund_me.withdraw({"from": account})
def get_bal(account=account):
    return fund_me.addressToAmountFunded(account)


def main():
    price_feed_address = get_mock()
    entrance_fee = fund_me.getEntranceFee()
    print(get_bal())
    fund(entrance_fee)
    print(get_bal())
    #withdraw()
    print(get_bal())
    pass


if __name__ == "__main__":
    main()
