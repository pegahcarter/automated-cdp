from py.api import INFURA, PRIVATE_KEY, PUBLIC_KEY
from web3 import Web3
import json

web = Web3(Web3.HTTPProvider(INFURA))

web.eth.getBalance(PUBLIC_KEY)
web.eth.defaultAccount = PUBLIC_KEY

transaction = {
    'to': '0x132DA98734146198b34AEfcb4D778ec14E2B6f0F',
    'value': 123,
    'gas': 21000,
    'gasPrice': 9* 10**9,
    'nonce': web.eth.getTransactionCount(web.eth.defaultAccount)
}

signed_tx = web.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

# This will send a transaction
# web.eth.sendRawTransaction(signed_tx.rawTransaction)

with open('data/abi/dai.json', 'r') as file:
    data = json.load(file)

erc20 = web.eth.contract(address='0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359', abi=data)


'https://etherscan.io/address/0x2D6C469497388239FE4fe4062A89C1EA68e1E84e#contracts'
