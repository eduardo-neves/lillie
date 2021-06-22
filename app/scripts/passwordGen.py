from passlib.hash import sha256_crypt
from datetime import datetime

password = sha256_crypt.hash("1234")

print(password)

print(sha256_crypt.verify("1234", password))

date = datetime.now()
print(date)