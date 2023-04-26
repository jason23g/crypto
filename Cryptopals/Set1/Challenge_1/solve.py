#!/usr/bin/env python3

import codecs
from base64 import b64encode, b64decode


s1 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# 1st solution

b64_1st_solution = codecs.encode(codecs.decode(s1, 'hex'), 'base64').decode()

print('Base64 result from 1st solution :', b64_1st_solution)

# 2nd solution


# hex -> base64
b64_2nd_solution = b64encode(bytes.fromhex(s1)).decode()
print('Base64 result from 2nd solution :', b64_2nd_solution)