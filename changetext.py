                                                #2. Encryption - cryptography - digital signature
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

key = rsa.generate_private_key(65537, 2048)
msg = b"I love Python!"
sig = key.sign(msg, padding.PKCS1v15(), hashes.SHA256())

try:
    key.public_key().verify(sig, msg, padding.PKCS1v15(), hashes.SHA256())
    print("Message   :", msg.decode())
    print("Signature :", sig.hex()[:40], "...")
    print("Status    : VALID ✅")
except:
    print("Status    : INVALID ❌")

# gui