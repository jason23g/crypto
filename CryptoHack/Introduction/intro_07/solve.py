from pwn import *

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"

key12 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"

key23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"

flag_key123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1_bytes = bytes.fromhex(key1)

key12_bytes = bytes.fromhex(key12)

key23_bytes = bytes.fromhex(key23)

flag_key123_bytes = bytes.fromhex(flag_key123)

res = xor(flag_key123_bytes,key23_bytes,key1_bytes)

print(res)
