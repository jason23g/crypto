#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes,bytes_to_long
from pwn import *

HOST = "mercury.picoctf.net"
PORT = 60368

r = remote(HOST, PORT)

response = r.readline()
response = r.readline()
response = r.readline()
response = r.readline()
response = r.readline().strip()

end = len(response)

n = int(response[3:end])
print("n:",n)

response = r.readline().strip()

end = len(response)
e = int(response[3:end])
print("e:",e)

response = r.readline().strip()

end = len(response)
c = response[12:end].decode('utf-8')
print("Ciphertext :",c)

x = pow(2,e,n)
print(x)
payload = c*x

r.recvuntil("Give me ciphertext to decrypt:")
r.sendline(payload)

response = r.readline().strip()

c2 = response[13:]

message = c2//2

print(long_to_bytes(message))
