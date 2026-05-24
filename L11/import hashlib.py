import hashlib
import json
from time import time

class Block(object):
    def __init__(self):
        self.chain = []
        self.newTransactions = []
        self.count = 0
        self.newBlock(prevHash = "no previous hash, since this is the first block", proof = 100)
    
    def newBlock(self, proof, prevHash = None):
        block = {
            "blockNo" : self.count,
            "timestamp" : time(),
            "transactions" : self.newTransactions or "no transactions, first genesis block",
            "gas fee" : 0.1,
            "nonce" : proof,
            "previous hash" : prevHash or self.hash(self.chain[-1])
        }

        self.newTransactions = []
        self.count += 1
        self.chain.append(block)
        return block

    def lastBlock(self):
        return self.chain[-1]

    def proofOfWork(self, prevProof):
        newProof = 1
        checkProof = False

        while not checkProof: # loop iterates until valid nonce is found
            compareProof = newProof**2 - prevProof**2 # used to generate a value to be hashed for proof of work
            string_compareProof = str(compareProof).encode() # convert calculated value to bytes for hashing
            encodeProof = hashlib.sha256(string_compareProof) # creates sha256 hash obj
            hashProof = encodeProof.hexdigest() # computes hexadecimal representation of hash

            if hashProof[0 : 4] == "0000":
                checkProof = True 
            else:
                newProof += 1

        return newProof

    def transaction(self, sender, recipient, amount): # adding a new transaction to list of transactions for current block
        senderEncoder = hashlib.sha256(sender.encode()) # anonymize sender by using hash instead of name to id
        senderHash = senderEncoder.hexdigest() # computes hexadecimal rep of sender's hash

        recipientEncoder = hashlib.sha256(recipient.encode())
        recipientHash = recipientEncoder.hexdigest()

        transactionData = {
            "sender" : senderHash,
            "recipient" : recipientHash,
            "amount" : amount
        }

        self.newTransactions.append(transactionData)
        return self.lastBlock

    def hash(self, block): #generate sha256 hash of given block
        stringObj = json.dumps(block, sort_keys=True) # ensures identical blocks produce same hash
        blockString = stringObj.encode()
        rawHash = hashlib.sha256(blockString)
        hexHash = rawHash.hexdigest()

        block["current hash"] = hexHash
        return hexHash

    def checkValidity(self, chain): # check validity of entire blockchain
        prevBlock = chain[0]
        blockIndex = 1

        while blockIndex < chain.length():
            currentBlock = chain[blockIndex]

            if currentBlock["previous hash"] != prevBlock["current hash"]:
                return False
            
            prevNonce = prevBlock["nonce"]
            currentNonce = currentBlock["nonce"]

            compareProof = currentNonce**2 - prevNonce**2
            string_compareProof = str(compareProof).encode()
            encodeProof = hashlib.sha256(string_compareProof)
            hashProof = encodeProof.hexdigest()

            if hashProof[0 : 4] != "0000":
                return False

            prevBlock = currentBlock
            blockIndex += 1

        return True

    
