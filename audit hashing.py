                                           #3. AUDIT - Hashing
import datetime
logs = [
    "User login: ali    - SUCCESS",
    "User login: hacker - FAILED",
    "File access: admin - SUCCESS",
    "User login: unknown - FAILED"
]
print("=== SECURITY AUDIT REPORT ===")
print("Date:", datetime.datetime.now())
for log in logs:
    status = "ALERT" if "FAILED" in log else "OK"
    print(f"{status} -> {log}")

# gui

import tkinter as tk
from tkinter import messagebox
import hashlib

# -------------------------------
# Default Username & Password
# username = admin
# password = Admin123
# -------------------------------

saved_username = "admin"

# Password Hash
saved_password = hashlib.sha256("Admin123".encode()).hexdigest()

# ================================
# LOGIN FUNCTION
# ================================

def login():

    username = entry_user.get()
    password = entry_pass.get()

    # Convert entered password to hash
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check username & password
    if username == saved_username and hashed_password == saved_password:

        messagebox.showinfo("Login", "Login Successful")

        open_dashboard()

    else:
        messagebox.showerror("Error", "Invalid Username or Password")

