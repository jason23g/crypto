#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
from pwn import *
 
def get_plaintext(param):
    r = requests.get('https://aes.cryptohack.org/ecbcbcwtf/decrypt/' + param)
    data = r.json()
    data = data['plaintext']
    return data


def get_ciphertext():
    r = requests.get('https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/')
    data = r.json()
    data = data['ciphertext']
    return data


def xor__hex_strings(a, b):
	result = int(a, 16) ^ int(b, 16) # convert to integers and xor them together
	return '{:x}'.format(result) 



ciphertext = get_ciphertext()
encrypted_flag = ciphertext[32:]
iv = ciphertext[:32]

plaintext  = xor__hex_strings(iv,get_plaintext(encrypted_flag[:32]))
plaintext += xor__hex_strings(get_plaintext(encrypted_flag[32:]),encrypted_flag[:32])

print(bytes.fromhex(plaintext).decode("utf-8"))
