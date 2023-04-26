from pwn import *
from Crypto.Util.number import *

a = 11
b = 6
c =8146798528947
d =17
res = min(a%b,c%d)
print("Result:",res)
