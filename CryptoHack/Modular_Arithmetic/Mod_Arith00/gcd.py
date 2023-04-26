from pwn import *
from Crypto.Util.number import *
import sys

def gcd(a,b):
 
 while b != 0:
  temp = b
  b = a%b
  a = temp

 return a



a = int(sys.argv[1]) #66528
b = int(sys.argv[2]) #52920
res = gcd(a,b)
print(res)


