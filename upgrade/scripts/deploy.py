#!/usr/bin/env python
from brownie import accounts, MonateV1, ProxyAdmin, TransparentUpgradeableProxy, MonateV2, Contract  # type: ignore
import eth_utils

def encode_function_data(intializer=None, *args):
    if len(args) == 0 or not intializer:
        return eth_utils.to_bytes(hexstr="0x")
    return intializer.encode_input(*args)


def deploys(deploy=False,function_data=None):
    account = accounts[0]
    if deploy:
        return (MonateV1.deploy({"from": account}),
                MonateV2.deploy({"from": account}),
                ProxyAdmin.deploy({"from": account}),
                TransparentUpgradeableProxy.deploy(
            MonateV1[-1].address, ProxyAdmin[-1].address, encode_function_data(function_data), {"from": account})

        )
    else:
        return (MonateV1[-1],MonateV2[-1],ProxyAdmin[-1],TransparentUpgradeableProxy[-1])

def upgrade(proxy,address,account,proxy_admin=ProxyAdmin[-1]):
    proxy_admin.upgrade(proxy,address,{"from":account}).wait(1)
    pass
def main():
    account = accounts[0]
    (monate_v1,monate_v2,proxy_admin,proxy) = deploys()
    print(monate_v1)
    print(proxy_admin)
    proxy_monate = Contract.from_abi("Monate", proxy.address, monate_v2.abi)
    print("current proxy imp: ",proxy_admin.getProxyImplementation(proxy.address))
    #(proxy_monate.modifyState(7,{"from":account})).wait(1)
    print("current state: ",proxy_monate.getState())
    #txn.wait(1)
    upgrade(proxy,monate_v2,account,proxy_admin)
    #proxy_monate.increment({"from":account})
    #(proxy_monate.modifyState(8,{"from":account})).wait(1)
    print("current state: ",proxy_monate.getState())