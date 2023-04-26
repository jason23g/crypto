from pwn import *
from Crypto.Util.number import *

x = "label"
n = 13

res = xor(x,n)

print(res)
