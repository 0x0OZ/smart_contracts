#!/usr/bin/env python
from brownie import accounts,config,SimpleStorage,network

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])
def main():
    account = get_account()
    print("acc: ",account)
    simple_storage = SimpleStorage.deploy({"from":account,"gas":855342,"gasPrice": 1000000000,})
    print("my acc: ",account)
    print("storage: ",simple_storage)
    #print(account)
    print(simple_storage.get())
    print(simple_storage.store(17,{"from":account}))
    print(simple_storage.get())

if __name__ == "__main__":
    main()
    