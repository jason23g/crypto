from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes



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

p_hex = "ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff"


g = bytes_to_long(bytes.fromhex(g_hex))

p = bytes_to_long(bytes.fromhex(p_hex))

C = pow(g,c,p)

D = pow(g,d,p)


print("C : ",long_to_bytes(C).hex())

print("D : ",long_to_bytes(D).hex())


iv = "3f7cd8d6957ede2e12e576e39b265506"

ciphertext = "03887815b2747e6f1bdbcdc1aad0086fc219c9989063cdf1982207e03b5934b0"

A_hex = "39c9ca671df0c12d5ee02d70e4fe9d0b26d473d57f59c787a182874dc2ca5efc5c4d2f0880954533382a987c11cd3493745865273f80d4e5d7563b0da7303d07996bd6e272c818c9dd569b13e154df3e3f6205c7cebeb59ce1e14cfdbab8a8d8f088656b7d4a29b9d0db6e98773a3603f18ac00efe1153ca1638231048488b1e2abceb6fb7e411310cfb72d9b25a22b0e4db50fd94747fd0e0dfbe526aaf9b50eb79761673a967348689b508ffccf3b1fd9afb660faf001a5397447e0758b8fe"

A = bytes_to_long(bytes.fromhex(A_hex))

sa = pow(A,d,p)

print(decrypt_flag(sa,iv,ciphertext))