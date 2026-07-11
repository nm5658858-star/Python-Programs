                                         #3. enc type - rsa - digital signature
import tkinter as tk
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

key = rsa.generate_private_key(65537,2048)
msg = b"saif"
sig = key.sign(msg,padding.PKCS1v15(),hashes.SHA256())

# Verify function
def verify_process():
    msg1 = msg_entry.get().encode()

    try:
        key.public_key().verify(sig,msg1,padding.PKCS1v15(),hashes.SHA256())
        result.config(text="Signature Verified ✔️", fg="blue")
    except:
        result.config(text="Not Verified ✘", fg="red")
root = tk.Tk()
root.title("Digital Signature App")
root.geometry("400x200")
tk.Label(root, text="Enter Message").pack(pady=(20, 5))
msg_entry = tk.Entry(root, width=40)
msg_entry.pack(pady=5)
tk.Button(root, text="Verify", command=verify_process, width=15).pack(pady=10)
result = tk.Label(root, text="", font=("Arial", 12, "bold"))
result.pack(pady=10)
root.mainloop()