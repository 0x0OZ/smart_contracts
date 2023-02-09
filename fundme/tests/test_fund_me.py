#!/usr/bin/env python
from brownie import accounts, FundMe, network, config, MockV3Aggregator  # type: ignore
from scripts.scripts import get_account
from scripts.deploy import deploy_fund_me
def test_fund_me():
    main()
def main():
    # Arrange - IDK - Assert
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    txn = fund_me.fund({"from": account, "value": entrance_fee})
    assert fund_me.addressToAmountFunded(account) == entrance_fee
    txn2 = fund_me.withdraw({"from": account})
    assert fund_me.addressToAmountFunded(account) == 0
    # IDK
    
    # Assert
    pass


if __name__ == "__main__":
    main()
