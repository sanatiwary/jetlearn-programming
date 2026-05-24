import hashlib
from hashlib import sha256
NONCE_LIMIT = 1000000000000
zeroes = 4

def mine(blockNo, transaction, prevHash):
    for nonce in range(NONCE_LIMIT):
        data = str(blockNo) + transaction + prevHash + str(nonce)
        hash = hashlib.sha256(data.encode()).hexdigest()
        print(hash)

        if hash.startswith('0' * zeroes):
            print("found the hash with 4 leading zeroes: ")
            print(nonce)
            return hash
    return -1

blockNo = 4
transaction = "bubbles"
prevHash = "1d92m0d03hf"

mine(blockNo, transaction, prevHash)
data = str(blockNo) + transaction + prevHash + str(187886)
hash = hashlib.sha256(data.encode()).hexdigest()

print(hash)