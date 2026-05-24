import hashlib
from time import time
import json
from hashlib import sha384

def block():
    transaction = {
        "receiver" : "thing1",
        "sender" : "thing2",
        "amount" : "77 ETN"
    }

    data = {
        "nonce" : "20456",
        "timestamp" : time(),
        "transaction" : transaction,
        "gasFee" : 0.1,
        "prevHash" : None
    }

    print('block info is ', data)
    stringData = json.dumps(data)
    print(stringData)
    print (type(stringData))

    result = hashlib.sha384(stringData.encode()).hexdigest()
    print(result)

block()