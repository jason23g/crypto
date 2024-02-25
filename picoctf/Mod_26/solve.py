#!/usr/bin/env python3

import codecs


ciphertext = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"

plaintext = codecs.decode(ciphertext, 'rot_13')

print(plaintext)