#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537
c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423



''' 
Go to factordb to facotrize n because its too small so it is posible to already have been factorized
n = p * q

'''

p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003

fn = (p-1)*(q-1)

d = inverse(e,fn)

m = pow(c,d,n)

plaintext = long_to_bytes(m)

print(plaintext)