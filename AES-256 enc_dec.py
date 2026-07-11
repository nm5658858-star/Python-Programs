import os, base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

msg = b"Hello Pakistan!"
key = os.urandom(32) 
nonce = os.urandom(16)

encryptor = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend()).encryptor()
encrypted = encryptor.update(msg)
decryptor = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend()).decryptor()
decrypted = decryptor.update(encrypted)

print("Original :", msg.decode())
print("Key :", key.hex())
print("Encrypted :", base64.b64encode(encrypted).decode())
print("Decrypted :", decrypted.decode())