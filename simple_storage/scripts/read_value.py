#!/usr/bin/env python
from brownie import accounts,SimpleStorage,config,network

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def get_value():
    account = get_account()
    simple_storage = SimpleStorage[-1]
    simple_storage.store(777,{"from":account})
    print(simple_storage.get())
def main():
    get_value()
    


if __name__ == "__main__":
    main()