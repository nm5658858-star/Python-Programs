import hashlib
msg = "I love Python!"
md5 = hashlib.md5(msg.encode()).hexdigest()
print(msg)
print("md5: ",md5)

sha1 = hashlib.sha1(msg.encode()).hexdigest()
print(msg)
print("sha1: ",sha1)

sha256 = hashlib.sha256(msg.encode()).hexdigest()
print(msg)
print("Sha256 :", sha256)

sha512 = hashlib.sha512(msg.encode()).hexdigest()
print(msg)
print("Sha512: ",sha512[:64])

sha3 = hashlib.sha3_256(msg.encode()).hexdigest()
print(msg)
print("Sha3: ", sha3)

blake2 = hashlib.blake2b(msg.encode()).hexdigest()
print(msg)
print("Blake2: ",blake2[:64])


#----------------------------------------
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
key = rsa.generate_private_key(65537, 2048)
msg = b"I love Python"
sig = key.sign(msg, padding.PKCS1v15(), hashes.SHA256())
try:
    key.public_key().verify(sig, msg, padding.PKCS1v15(), hashes.SHA256())
    print("Message: ", msg.decode())
    print("Sign: ", sig.hex()[:40])
    print("Valid")
except:
    print("Invalid")
#----------------------------------------
import tkinter as tk
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
key = rsa.generate_private_key(65537, 2048)
msg = b"saif"
sig = key.sign(msg, padding.PKCS1v15(), hashes.SHA256())

def verify_sig():
    msg1 = msg_entry.get().encode()

    try:
        key.public_key().verify(sig,msg1,padding.PKCS1v15(),hashes.SHA256())
        result.config(text = "Verified", fg = "blue")
    except:
        result.config(text = "Unverified", fg = "red")
root = tk.Tk()
root.title("Digital signature")
root.geometry("400x200")
tk.Label(root, text = "Enter message: ").pack(pady = (20,5))
msg_entry = tk.Entry(root, text = "", width = 40)
msg_entry.pack(pady = (10))
tk.Button(root, text = "Verify", command = verify_sig, width = 10).pack(pady = 5)
result = tk.Label(root, text = "", font = ("arial",12,"bold"))
result.pack(pady = 8)
root.mainloop()


#--------------------------------------------
import datetime
logs = [
             "User login: Ali - Success",
             "User login: Hacker - Failed",
             "File access: Admin - Success",
             "User login: Unknown - Failed"
        ]
print("=== Audit Hashing ===")
print(datetime.datetime.now())
for log in logs:
    status = "Alert!" if "Failed" in log else "OK"
    print(f"{status} -> {log}")
    
#-----------------------------------------------------
import os, base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms,modes
from cryptography.hazmat.backends import default_backend

msg = b"JIO"
key = os.urandom(32)
Nonce = os.urandom(16)

encryptor = Cipher(algorithms.AES(key), modes.CTR(Nonce), backend = default_backend()).encryptor()
encrypted = encryptor.update(msg)
decryptor = Cipher(algorithms.AES(key), modes.CTR(Nonce), backend = default_backend()).decryptor()
decrypted = decryptor.update(encrypted)

print("Original: ", msg.decode())
print("Key: ", key.hex())
print("Encrypted: ", base64.b64encode(encrypted).decode())
print("Decrypted: ", decrypted.decode())

#--------------------------------------------
from cryptography.fernet import Fernet 
key = Fernet.generate_key() 
cipher = Fernet(key) 
message = b"Hello Pakistan" 
encrypted = cipher.encrypt(message) 
print(encrypted) 
decrypted = cipher.decrypt(encrypted) 
print(decrypted.decode()) 

#-----------------------------------------------


key = input("Enter key:")
text = input("Enter text: ")
encrypted = ""
for ch in text:
     encrypted += chr(ord(ch) + 1)
print("Encrypted: ",encrypted)

decrypted = ""
for ch in encrypted:
     decrypted += chr(ord(ch) - 1)
print("Decrypted: ",decrypted)