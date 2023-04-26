#!/usr/bin/env python3

import codecs
from base64 import b64encode, b64decode

def xor_single_char(s1,s2):
    
    bytes_s1 = bytes.fromhex(s1)

    xor_res = bytes_s1 ^ binary_s2
    return hex(xor_res)[2:]


def findKey(s1):

    for i in range(255):
        s2 = str(i)
        tmp_res = xor_strings(s1,s2)
        print(i)
        try:
            print(bytes.fromhex(tmp_res).decode("utf-8"))
        except:
            print("Something went wrong")
        else:
            print("This string cant be decoded")




s1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"




findKey(s1)
