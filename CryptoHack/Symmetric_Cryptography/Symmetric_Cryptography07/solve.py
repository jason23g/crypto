import requests

r = requests.get('http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')

ciphertext_json = r.json()


ciphertext = ciphertext_json["ciphertext"]

r = requests.get('http://aes.cryptohack.org/block_cipher_starter/decrypt/'+ciphertext+'/')

plaintext_json = r.json()

plaintext = plaintext_json["plaintext"]

print(bytes.fromhex(plaintext))