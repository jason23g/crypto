from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
 
def get_request(param):
    r = requests.get('https://aes.cryptohack.org/ecb_oracle/encrypt/' + param)
    data = r.json()
    data = data['ciphertext']
    return data
 
# list with strings from "01" to "FF"
byte_list = []
for i in range(1, 256):
    b = hex(i)[2:]
    if len(b) == 1:
        b = '0' + b
    byte_list.append(b)
 
offset = 'AA' * 7 + 'AA' * 16
payload = offset
pad_count = 15
flag = '6e3675316e355f683437335f3363627d'
blank_block = '0bb6c010152c5f9b9051ba9c5a2d6f85'
 
 
def get_padding(length):
    return byte_list[length - 1]
 
while len(flag) < 50:
    payload += 'AA'
    ciphertext = get_request(payload)
    last_block = ciphertext[-64:-32]
 
    if last_block == blank_block:
        last_block = ciphertext[-64: -32]
        pad_count = 16
 
    for b in byte_list:
        # get the very first block where our input is going to be
        inp = b + flag + get_padding(pad_count) * pad_count
        result = get_request(inp)
        print("testing: " + inp)
        first_block = result[:32]
        if first_block == last_block:
            print("FOUND: " + b)
            flag = b + flag
            break
 
    pad_count -= 1
 
print("flag: ", end="")
print(bytes.fromhex(flag))

