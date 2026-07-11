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
# ===============================
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
# ================================
# DASHBOARD WINDOW
# ================================
def open_dashboard():
    dashboard = tk.Toplevel(root)
    dashboard.title("Audit Security Dashboard")
    dashboard.geometry("500x300")
    dashboard.configure(bg="#dff9fb")
    title = tk.Label(
        dashboard,
        text="Audit Security Dashboard",
        font=("Arial", 18, "bold"),
        bg="#dff9fb",
        fg="darkblue"
    )
    title.pack(pady=20)
    info = tk.Label(
        dashboard,
        text="""
Welcome Admin
Security Features:
✔ Secure Login
✔ Password Hashing
✔ Audit Access
✔ Protected Dashboard
        """,
        font=("Arial", 12),
        bg="#dff9fb",
        justify="left"
    )
    info.pack(pady=10)
    logout_btn = tk.Button(
        dashboard,
        text="Logout",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        width=12,
        command=dashboard.destroy
    )
    logout_btn.pack(pady=20)
# ===============================
# MAIN WINDOW
# ================================
root = tk.Tk()
root.title("Audit Security App")
root.geometry("400x300")
root.configure(bg="#f5f6fa")
title = tk.Label(
    root,
    text="Audit Security Login",
    font=("Arial", 18, "bold"),
    bg="#f5f6fa",
    fg="darkblue"
)
title.pack(pady=20)
label_user = tk.Label(
    root,
    text="Username",
    font=("Arial", 12),
    bg="#f5f6fa"
)
label_user.pack()
entry_user = tk.Entry(root, font=("Arial", 12))
entry_user.pack(pady=5)
# Password
label_pass = tk.Label(
    root,
    text="Password",
    font=("Arial", 12),
    bg="#f5f6fa"
)
label_pass.pack()
entry_pass = tk.Entry(root, show="*", font=("Arial", 12))
entry_pass.pack(pady=5)
# Login Button
login_btn = tk.Button(
    root,
    text="Login",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=15,
    command=login
)
login_btn.pack(pady=20)
# Run App
root.mainloop()