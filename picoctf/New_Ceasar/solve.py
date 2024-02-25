#!/usr/bin/env python3

import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(enc):
	
	plaintext = ""

	#print(len(enc))

	for i in range(0,len(enc),2):

		#print(i)


		index1 = ALPHABET.find(enc[i])
		index2 = ALPHABET.find(enc[i+1])
		#print(index1)
		#print(index2)
		bin1 = format(index1, '04b')
		bin2 = format(index2, '04b')
		#print(bin1)
		#print(bin2)
		binary = bin1+bin2
		#print(binary)
		#print(int(str(binary),2))
		plaintext += "".join(chr(int(str(binary),2)))

	return plaintext


def rev_shift(c, k):
	t1 = ord(c) + LOWERCASE_OFFSET
	t2 = ord(k) + LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]


ciphertext = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"

for key in ALPHABET :
	plaintext = ""
	for i, c in enumerate(ciphertext):
		plaintext += "".join(rev_shift(c, key[i % len(key)]))

	#print(key)
	#print(b16_decode(plaintext))
	print("picoCTF{",b16_decode(plaintext),"}")



