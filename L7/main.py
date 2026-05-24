import hashlib
from time import time
from hashlib import sha256
import json

class Block ():
    def __init__(self):
        self.chain = []
        self.newTransactions = []
        self.count = 0
        self.newBlock(prevHash = "none")
    def newBlock(self, prevHash = None):
        block = {
            'block no.' : self.count,
            'timestamp' : time(),
            'transaction': self.newTransactions or 'no transaction will be stored for the first genesis block',
            "gasFee" : 0.4,
            "prevHash" : prevHash or self.hash(self.chain[-1])
        }

        self.count += 1
        self.newTransactions = []
        self.chain.append(block)
        return block

    def lastBlock(self):
        return self.chain[-1]

    def transaction(self, sender, receiver, amount):
        senderEncode = hashlib.sha256(sender.encode()).hexdigest()
        receiverEncode = hashlib.sha256(receiver.encode()).hexdigest()
        
        data = {
            "sender" : senderEncode,
            "receiver" : receiverEncode,
            "amount" : amount
        }

        self.newTransactions.append(data)

        return self.lastBlock

    def hash(self, block):
        stringData = json.dumps(block)
        hexHash = hashlib.sha256(stringData.encode()).hexdigest()
        block['current hash'] = hexHash
        return hexHash

blockchain = Block()

t1 = blockchain.transaction("billy", "bob", 14)

t2 = blockchain.transaction("ruth", "joe", 31)

t3 = blockchain.transaction("toe", "finger", 12)
blockchain.newBlock()

print(blockchain.chain)