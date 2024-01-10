import hashlib

string = input()

result = hashlib.sha256(string.encode()).hexdigest()

print(result)