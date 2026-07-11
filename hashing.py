                                                    #1. hasing
import hashlib 
msg = "Hello Pakistan!" 
md5 = hashlib.md5(msg.encode()).hexdigest() 
print("=== MD5 ===") 
print("Original :", msg) 
print("Hash    :", md5)

sha1 = hashlib.sha1(msg.encode()).hexdigest() 
print("=== SHA1 ===") 
print("Original :", msg) 
print("Hash    :", sha1)

sha256 = hashlib.sha256(msg.encode()).hexdigest() 
print("=== SHA256 ===") 
print("Original :", msg) 
print("Hash    :", sha256)


sha512 = hashlib.sha512(msg.encode()).hexdigest() 
print("=== SHA512 ===") 
print("Original :", msg) 
print("Hash    :", sha512)

sha3 = hashlib.sha3_256(msg.encode()).hexdigest() 
print("=== SHA3 ===") 
print("Original :", msg) 
print("Hash    :", sha3)

blake2 = hashlib.blake2b(msg.encode()).hexdigest() 
print("\n=== BLAKE2 ===") 
print("Original :", msg) 
print("Hash: ", blake2[:64], "...")
