#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests

def encrypt():
    r = requests.get('https://aes.cryptohack.org/bean_counter/encrypt/')
    data = r.json()
    data = data['encrypted']
    return data

def xor__hex_strings(a, b):

    bin_a = bytes.fromhex(a)
    bin_b = bytes.fromhex(b)
    i = 0

    out = [0]*len(bin_a)
    while i < len(bin_a):

        out[i] = bin_a[i]^bin_b[i]
        i = i + 1


    return bytes(out).hex()

png_header = "89504e470d0a1a0a0000000d49484452"
cipher = encrypt()
key = xor__hex_strings(png_header,cipher[:32])
keystream = bytes.fromhex(key)


ciphertext = bytes.fromhex(cipher)
i = 0;
out = [0]*len(ciphertext)
while i < len(ciphertext):

    out[i] = ciphertext[i]^keystream[i%len(keystream)]
    i = i +1;


f = open("bean_flag.png", "wb")
f.write(bytes(out))
f.close()