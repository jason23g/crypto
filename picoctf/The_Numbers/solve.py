#!/usr/bin/env python3


numbers = [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]

plaintext = ""

for i in range(len(numbers)):


	plaintext += "".join(chr(numbers[i]+96))

	if(i == 6):
		plaintext += "{"

	if( i == len(numbers)-1):
		plaintext+="}"


print(plaintext)
