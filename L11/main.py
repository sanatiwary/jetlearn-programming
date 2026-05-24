import datetime
import hashlib

class Block ():
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    prevHash = 0x0
    timestamp = datetime.datetime.now()

    def __init__ (self, data):
        self.data = data
    
    def hash (self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.prevHash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )

        return h.hexdigest()

    def __str__(self):
        return "blockhash: " + str(self.hash()) + "\n blockNo: " + str(self.blockNo) + "\n block data: " + str(self.data) + "\n hash: " + str(self.nonce) + "\n"

class Blockchain ():
    diff = 45
    maxNonce = 2 ** 32
    target = 2 ** (256 - diff)

    block = Block("genesis")
    dummy = head = block

    def add (self, block):
        block.prevHash = self.block.hash
        block.blockNo = self.block.blockNo + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()
for n in range(10):
    blockchain.mine(Block("block: " + str(n + 1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next