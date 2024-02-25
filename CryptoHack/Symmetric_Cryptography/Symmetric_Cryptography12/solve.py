#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests

def encrypt_flag():
    r = requests.get('https://aes.cryptohack.org/symmetry/encrypt_flag')
    data = r.json()
    data = data['ciphertext']
    return data


def encrypt(plaintext,iv):
    r = requests.get('https://aes.cryptohack.org/symmetry/encrypt/'+plaintext+'/'+iv+'/')
    data = r.json()
    data = data['ciphertext']
    return data


def xor__hex_strings(a, b):
	result = int(a, 16) ^ int(b, 16) # convert to integers and xor them together
	return '{:x}'.format(result) 





ciphertext = encrypt_flag()
encrypted_flag = ciphertext[32:]
iv = ciphertext[:32]


print(bytes.fromhex(encrypt(encrypted_flag,iv)).decode("utf-8"))