#!/usr/bin/env python
from brownie import accounts, FundMe, network, config, MockV3Aggregator # type: ignore
from scripts.scripts import get_account, get_mock

account = get_account()
def deploy_fund_me():
    price_feed_address = get_mock()
    fund_me = FundMe.deploy(price_feed_address, {
                            "from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to: {fund_me.address}")
    return fund_me
def main():
    print(f"The Active net: {network.show_active()}")
    deploy_fund_me()

if __name__ == "__main__":
    main()
