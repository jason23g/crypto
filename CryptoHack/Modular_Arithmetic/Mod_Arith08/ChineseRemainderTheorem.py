from pwn import *
from Crypto.Util.number import *

'''
Looking at Chinese Remainder Theorem...
Taken
        x = a1 (mod n1)
        x = a2 (mod n2)
        x = a3 (mod n3)
With gcd(n1,n2) = gcd(n1,n3) = gcd(n2,n3) = 1
        -All the n-values are coprime with the others
We have N = n1*n2*n3 and
        N1 = n2*n3
        N2 = n1*n3
        N3 = n1*n2
Summaring, the Ni values are composed multiplying all
the n-values each others, except n at position i
Ending, we call yi the solutions of Ni*yi = 1 (mod ni)
        Ex: N1 * y1 = 1 (mod n1)
Now, we have to find the value of integer a such that:
        x = a (mod N)
Knowing also that:
        x = a1N1y1 + a2N2y2 + a3N3y3 (mod N)
'''
# x = 2 mod 5
# x = 3 mod 11
# x = 5 mod 17

# x = a mod 935

length = 3
a = [2,3,5]
n = [5,11,17]

Ntot= n[0] * n[1] * n[2]

N = [ n[1]*n[2] , n[0]*n[2], n[0]*n[1] ]

y = [pow(N[i],n[i]-2,n[i]) for i in range(length)]

mysterious_a = 0
for i in range(length):
        mysterious_a += a[i]*N[i]*y[i]
mysterious_a %= Ntot
print(mysterious_a)


