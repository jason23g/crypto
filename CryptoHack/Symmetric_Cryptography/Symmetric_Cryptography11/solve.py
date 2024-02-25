'''

cookie : b243b5fda450514c512b47840deff508
		 82dc463efca47adffe54c8ea0de3e42c
		 b753e8224d988052900607584855b62a



iv : b243b5fda450514c512b47840deff508
	 00000000000012131916650000000000
		 
1st block ->	82dc463efca47adffe54c8ea0de3e42c
				00000000000012131916650000000000  XOR : 82dc463efca468cce742adea0de3e42c

admin=True : 61646d696e3d5472756565
admin=False: 61646d696e3d46616c7365   -> XOR : 0000000000001213191600



2nd block ->	b753e8224d988052900607584855b62a
				12131916121319161213191612131916
				00000000000012131916650000000000 XOR :b753e8224d989241891062584855b62a


				82dc463efca468cce742adea0de3e42cb753e8224d988052900607584855b62a


crypto{4u7h3n71c4710n_15_3553n714l}


'''

#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
from pwn import *
 
def get_cookie():
    r = requests.get('https://aes.cryptohack.org/flipping_cookie//get_cookie/')
    data = r.json()
    data = data['cookie']
    return data


def check_admin(iv,cookie):
    r = requests.get('https://aes.cryptohack.org/flipping_cookie/check_admin/'+cookie+'/'+iv+'/')
    data = r.json()
    data = data['flag']
    return data


def xor__hex_strings(a, b):
	result = int(a, 16) ^ int(b, 16) # convert to integers and xor them together
	return '{:x}'.format(result) 





cookie = get_cookie()
encrypted_flag = cookie[32:]
iv = cookie[:32]

flip_payload = "000000000000121319165e0000000000"

flipped_cookie = xor__hex_strings(iv[:32],flip_payload)


print(check_admin(flipped_cookie,encrypted_flag))
