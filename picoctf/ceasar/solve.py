#!/usr/bin/env python3

import codecs

ciphertext = "ynkooejcpdanqxeykjrbdofgkq"

plaintext = codecs.decode(ciphertext, 'ceasar')

print("picoCTF{"+plaintext+"}")