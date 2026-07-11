#import hashlib
#text = input("Enter a text: ")
#hash_obj = hashlib.md5(text.encode())

#print(hash_obj.hexdigest())


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