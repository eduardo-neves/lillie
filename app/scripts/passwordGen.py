from passlib.hash import sha256_crypt

password = sha256_crypt.hash("1234")

print(password)

print(sha256_crypt.verify("1234", password))
