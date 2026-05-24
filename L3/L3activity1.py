from datetime import datetime, date

class Block:
    def __init__(self, data, prevHash, nonce, timestamp):
        self.data = data
        self.prevHash = prevHash
        self.nonce = nonce
        self.timestamp = timestamp

today = date.today()
#dd/mm/yyyy
d1 = today.strftime("%d/%m/%Y")
#mm/dd/yyyy
d2 = today.strftime("%m/%d/%Y")
#mm/dd/yy
d3 = today.strftime("%m/%d/%y")

now = datetime.now()
d4 = now.strftime("%H:%M:%S %m/%d/%y")
timestamp = d4

data = {"from" : "sana",
        "to" : "ava",
        "coins" : "15"}
prevHash = "00007b2l3u4e0P4h2l9o8x7"
nonce = 75302

b1 = Block(data, prevHash, nonce, timestamp)
print(b1.timestamp)