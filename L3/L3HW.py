from datetime import datetime, date

class Example:
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
timestamp = d2

data = {"from" : "mosh",
        "to" : "bob",
        "coins" : "23"}
prevHash = "29293jn982911e3f8"
nonce = 23014

b2 = Example(data, prevHash, nonce, timestamp)
print(b2.data)