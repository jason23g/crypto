from pwn import *
from Crypto.Util.number import *


flag = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

flag_bytes = bytes.fromhex(flag)


for i in range(255):
 key =  i
 res = xor(flag_bytes,key)
 print(res)
