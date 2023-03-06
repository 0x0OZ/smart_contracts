#!/usr/bin/env python
from brownie import accounts,SimpleStorage

def test_deploy():
    # Arrage
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from":account})
    starting_value = simple_storage.get()
    excepted = 777
    # Assert
    assert excepted == starting_value