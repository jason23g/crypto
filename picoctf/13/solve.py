#!/usr/bin/env python3

import codecs


ciphertext = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

plaintext = codecs.decode(ciphertext, 'rot_13')

print(plaintext)
