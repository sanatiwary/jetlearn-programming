import hashlib
from hashlib import sha256

text = "Sun is shining"
result = hashlib.sha256(text.encode()).hexdigest()
print(result)

result = hashlib.sha384(text.encode()).hexdigest()
print(result)

result = hashlib.sha3_256(text.encode()).hexdigest()
print(result)