from pwn import *
from Crypto.Util.number import *

secret = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

secret_bytes = bytes.fromhex(secret)

key1 = "crypto{"

res1 = xor(secret_bytes,key1)
res1_string = res1.decode()
print(res1_string)


key1 = "myXORkey"

res1 = xor(secret_bytes,key1)
res1_string = res1.decode()
print(res1_string)


