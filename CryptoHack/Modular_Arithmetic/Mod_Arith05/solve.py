from pwn import *
from Crypto.Util.number import *
'''
Looking again at Fermat's little theorem...
if p is prime, for every integer a:
        pow(a, p) = a mod p
and, if p is prime and a is an integer coprime with p:
        pow(a, p-1) = 1 mod p
We can do some magic like this:
Note: i'll use math notation, so a^b means pow(a,b)
        a^(p-1) = 1 (mod p)
        a^(p-1) * a^-1 = a^-1 (mod p)
        a^(p-2) * a * a^-1 = a^-1 (mod p)
        a^(p-2) * 1 = a^-1 (mod p)
So finally we have:
        a^(p-2) = a^-1 (mod p)
So, doing a^(p-2) and then (mod p) we can achieve
our result
'''


ints = [14,6,11]
p = 29
temp = 30

for i in range(0,p-1):
 res = pow(i,2,p)
 if res == ints[0] or res == ints[1] or res == ints[2]:
  temp = min(temp,i)


print("Minimum square root is ",temp)
