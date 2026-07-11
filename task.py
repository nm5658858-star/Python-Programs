import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def run_aes_demonstration():
    original_message = b"This message demonstrates secure AES encryption using Python."
    

    secret_key = os.urandom(32)
    

    nonce = os.urandom(16)


    cipher = Cipher(algorithms.AES(secret_key), modes.CTR(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(original_message) + encryptor.finalize()


    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

    print("--- AES-256 CTR Mode Demonstration ---")
    print(f"Secret Key (Hex):  {secret_key.hex()}")
    print(f"Ciphertext (Hex):  {ciphertext.hex()}")
    print(f"Decrypted Message: {decrypted_message.decode('utf-8')}")
    
    print("\n--- Metadata & Sizes ---")
    print(f"Secret Key Size:   {len(secret_key)} bytes")
    print(f"Ciphertext Size:   {len(ciphertext)} bytes")
    print(f"Nonce Size:        {len(nonce)} bytes")

    # Final Verification
    if original_message == decrypted_message:
        print("\nSuccess: The decrypted message matches the original exactly.")
    else:
        print("\nError: Decryption failed.")

if __name__ == "__main__":
    run_aes_demonstration()