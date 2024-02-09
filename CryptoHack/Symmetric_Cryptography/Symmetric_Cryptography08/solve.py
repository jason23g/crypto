import requests
import hashlib
import random

r = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')

ciphertext_json = r.json()

ciphertext = ciphertext_json["ciphertext"]

print(ciphertext)

with open("words") as f:
    words = [w.strip() for w in f.readlines()]


for keyword in words:

 KEY = hashlib.md5(keyword.encode()).digest()


 r = requests.get('http://aes.cryptohack.org/passwords_as_keys/decrypt/'+ciphertext+'/'+KEY.hex()+'/')

 plaintext_json = r.json()

 plaintext = plaintext_json["plaintext"]

 if b'crypto' in bytes.fromhex(plaintext):
 	print("FOUND")
 	print(bytes.fromhex(plaintext))
 	break
