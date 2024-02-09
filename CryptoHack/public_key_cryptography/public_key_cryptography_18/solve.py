from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
from sympy.ntheory import discrete_log


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

c = 3 
d = 5 

g_hex = "02"

p_hex = "de26ab651b92a129"

B_hex = "43455b1d935410da"


g = bytes_to_long(bytes.fromhex(g_hex))

p = bytes_to_long(bytes.fromhex(p_hex))

B = bytes_to_long(bytes.fromhex(B_hex))

b = discrete_log(p,B,g)
 #s \log_7(15) (mod 41 
 # discrete_log(41, 15, 7)




iv = "be2ba2a48fe8aa0071c2c8b09aad2976"

ciphertext = "c1058a452706c412207e200184996b2868a501360a712d43b398b36538c9a8e0"

A_hex = "3e5725536c80cb45"

A = bytes_to_long(bytes.fromhex(A_hex))

sa = pow(A,b,p)

print(decrypt_flag(sa,iv,ciphertext))