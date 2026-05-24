from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

if w3.is_connected():
    print('connected!')
else:
    print('please check account connection')

def balance(address):
    bal = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(bal, "ether")
    print(f"the balance of account {address} is {balance_eth}")

balance("0x100C5A23E16842B0c958B230bF7aD4889319CcD4")

nonce = w3.eth.get_transaction_count("0x100C5A23E16842B0c958B230bF7aD4889319CcD4")

transaction = {
    "nonce" : nonce,
    "to" : "0x947010852E3ea90729e5CF5D33a018a66505e125",
    "value" : w3.to_wei(10, 'ether'),
    "gas" : 200000,
    "gasPrice" : w3.to_wei(50, "gwei")
}

signing = w3.eth.account.sign_transaction(transaction, "0x092140bc189e3f3d1ecf0dbdf495744540b645d846aaaa4618b610b6d6bb1b8a")
txHash = w3.eth.send_raw_transaction(signing.rawTransaction)

print(w3.to_hex(txHash))
balance("0x100C5A23E16842B0c958B230bF7aD4889319CcD4")

balance("0x33eE7faE0e1b1d13BD85aB15A94Fd2f3E7226d29")

nonce = w3.eth.get_transaction_count("0x33eE7faE0e1b1d13BD85aB15A94Fd2f3E7226d29")

transaction = {
    "nonce" : nonce,
    "to" : "0xf2800bcC848cfAfD4cB84AC44FE80E0562D178fD",
    "value" : w3.to_wei(10, 'ether'),
    "gas" : 200000,
    "gasPrice" : w3.to_wei(50, "gwei")
}

signing = w3.eth.account.sign_transaction(transaction, "0x5ff8c3496da2d4f0cbf19c9be1808e10f1cda95d062d834cf6c7d2d169a566dc")
txHash = w3.eth.send_raw_transaction(signing.rawTransaction)

print(w3.to_hex(txHash))
balance("0x33eE7faE0e1b1d13BD85aB15A94Fd2f3E7226d29")
