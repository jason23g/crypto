from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta


KEY = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'
FLAG = b"crypto{secret_flag}" 

def check_admin(cookie, iv):
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)

    try:
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cookie)
        print(decrypted)
        unpadded = unpad(decrypted, 16)
    except ValueError as e:
        return {"error": str(e)}

    print(unpadded.split(b";"))

    if b"admin=True" in unpadded.split(b";"):
        print(FLAG)
        return {"flag": FLAG}
    else:
        return {"error": "Only admin can read the flag"}


def get_cookie():
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    cookie = f"admin=False;expiry={expires_at}".encode()

    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    ciphertext = iv.hex() + encrypted.hex()

    return {"cookie": ciphertext}

first_block = "969d23d1d2880c20fd8fc64e0b9540aa"

## 969d23d1d2880c20fd8fc64e0b9540aa ^ 0000000000001213191600000000000

#first_block = "969d23d1d2881e33e499c64e0b9540aa"

second_block = "d9ee6bb996d5e87b29f7e497d212b895"

# d9ee6bb996d5e87b29f7e497d212b895 ^ 000000000000121319165e0000000000

#second_block = "d9ee6bb996d5fa6830e1e497d212b895"

#iv = "723a1f11b327fb80d537f47ec2030706" 

iv = "723a1f11b327e993cc21aa7ec2030706"


cookie = first_block+second_block

print(first_block)
print(second_block)
print(iv)

print(check_admin(cookie,iv))

crypto{4u7h3n71c4710n_15_3553n714l}
