#!/usr/bin/env python3

def xor_strings(s1, s2):

    binary_s1 = int(s1, 16)
    binary_s2 = int(s2, 16)

    xor_res = binary_s1 ^ binary_s2
    return hex(xor_res)[2:]



s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"

res = xor_strings(s1,s2)

print(res)
