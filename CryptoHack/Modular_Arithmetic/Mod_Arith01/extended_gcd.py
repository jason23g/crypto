from pwn import *
from Crypto.Util.number import *

'''

p * u + q * v = gcd(p,q)

'''

def extended_gcd(a,b):
 s = 0
 old_s = 1
 old_r = a
 r = b

 while r != 0:
  quotient = old_r//r
  prev_r = r
  r = old_r - quotient*prev_r
  old_r = prev_r
  prev_s = s
  s = old_s - quotient*prev_s
  old_s = prev_s

 if b!= 0:
  bezout_t = (old_r-old_s*a) // b;
 else:
  bezout_t = 0;

 return (old_s,bezout_t)



a = int(sys.argv[1]) #26513
b = int(sys.argv[2]) #32321

(c,d) = extended_gcd(a,b)
print("c:",c)
print("d:",d)
