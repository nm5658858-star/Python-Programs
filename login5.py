import hashlib
import datetime
import random
import tkinter as tk
import os

ACCOUNTS_FILE = "accounts.txt"
KEYS_FILE = "keys.txt"
LOGS_FILE = "logs.txt"

def create_session():
    return random.randint(1000, 9999)

# --- File Utilities ---

def load_file_to_dict(file_path):
    data_dict = {}
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if line and ":" in line:
                    k, v = line.split(":", 1)
                    data_dict[k] = v
    return data_dict

def append_to_file(file_path, k, v):
    with open(file_path, "a") as file:
        file.write(f"{k}:{v}\n")

def append_log_to_file(log_entry):
    with open(LOGS_FILE, "a") as file:
        file.write(log_entry + "\n")

# --- Custom Stylish Message Box ---

def custom_message(title, message, bg_color, button_color):
    popup = tk.Toplevel()
    popup.title(title)
    popup.geometry("360x200")
    popup.configure(bg=bg_color)
    popup.resizable(False, False)

    tk.Label(
        popup,
        text=title,
        font=("Helvetica", 15, "bold"),
        bg=bg_color,
        fg="white"
    ).pack(pady=15)

    tk.Label(
        popup,
        text=message,
        font=("Helvetica", 11),
        bg=bg_color,
        fg="white",
        wraplength=300,
        justify="center"
    ).pack(pady=10)

    tk.Button(
        popup,
        text="OK",
        command=popup.destroy,
        bg=button_color,
        fg="white",
        font=("Helvetica", 10, "bold"),
        width=10,
        relief="flat"
    ).pack(pady=15)

# --- Secondary Key Verification Window ---

def open_key_verification_window(username):
    key_window = tk.Toplevel(root)
    key_window.title("Security Verification")
    key_window.geometry("380x250")
    key_window.configure(bg="#f4f6f9")
    key_window.resizable(False, False)

    tk.Label(
        key_window,
        text="ENTER SECRET KEY",
        font=("Helvetica", 14, "bold"),
        bg="#f4f6f9",
        fg="#2c3e50"
    ).pack(pady=15)

    tk.Label(
        key_window,
        text=f"Verification required for user: {username}",
        font=("Helvetica", 10, "italic"),
        bg="#f4f6f9",
        fg="#7f8c8d"
    ).pack(pady=5)

    key_entry = tk.Entry(
        key_window,
        font=("Helvetica", 11),
        width=24,
        show="*"
    )
    key_entry.pack(pady=15)

    def verify_key_action():
        secret_key = key_entry.get().strip()

        if not secret_key:
            custom_message(
                "Warning",
                "Secret Key field cannot be empty!",
                "#f39c12",
                "#d35400"
            )
            return

        encrypted_key = hashlib.sha256(secret_key.encode()).hexdigest()
        keys_database = load_file_to_dict(KEYS_FILE)

        if username in keys_database and keys_database[username] == encrypted_key:
            session_id = create_session()
            login_time = datetime.datetime.now()

            log_line = f"{login_time.strftime('%d-%m-%Y %H:%M:%S')} -> LOGIN SUCCESS -> {username}"
            append_log_to_file(log_line)

            success_msg = (
                f"Login Successful!\n\n"
                f"Welcome: {username}\n"
                f"Session ID: {session_id}\n"
                f"Login Time: {login_time.strftime('%H:%M:%S')}"
            )

            custom_message(
                "Welcome",
                success_msg,
                "#3498db",
                "#2980b9"
            )
            key_window.destroy()
        else:
            now = datetime.datetime.now()
            log_line = f"{now.strftime('%d-%m-%Y %H:%M:%S')} -> LOGIN FAILED (Invalid Secret Key) -> {username}"
            append_log_to_file(log_line)

            custom_message(
                "Login Failed",
                "Verification failed. Incorrect Secret Key.",
                "#e74c3c",
                "#c0392b"
            )
            key_window.destroy()

    tk.Button(
        key_window,
        text="Verify & Enter",
        command=verify_key_action,
        bg="#3498db",
        fg="white",
        font=("Helvetica", 11, "bold"),
        width=18,
        pady=5,
        relief="flat"
    ).pack(pady=10)

# --- Main Window GUI Functions ---

def handle_create_account():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    secret_key = master_key_entry.get().strip()

    if not username or not password or not secret_key:
        custom_message(
            "Warning",
            "All fields (Username, Password, and Key) must be filled!",
            "#f39c12",
            "#d35400"
        )
        return

    accounts_database = load_file_to_dict(ACCOUNTS_FILE)

    if username in accounts_database:
        custom_message(
            "Error",
            "Username already exists!",
            "#e74c3c",
            "#c0392b"
        )
        return

    # Encrypt data using SHA-256 hashes
    encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    encrypted_key = hashlib.sha256(secret_key.encode()).hexdigest()
    
    # Write entries to their respective separate text files
    append_to_file(ACCOUNTS_FILE, username, encrypted_password)
    append_to_file(KEYS_FILE, username, encrypted_key)

    now = datetime.datetime.now()
    log_line = f"{now.strftime('%d-%m-%Y %H:%M:%S')} -> ACCOUNT CREATED -> {username}"
    append_log_to_file(log_line)

    custom_message(
        "Success",
        "Account Created Successfully!",
        "#2ecc71",
        "#27ae60"
    )

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    master_key_entry.delete(0, tk.END)

def handle_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        custom_message(
            "Warning",
            "Please enter both Username and Password!",
            "#f39c12",
            "#d35400"
        )
        return

    encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    accounts_database = load_file_to_dict(ACCOUNTS_FILE)

    # First Stage Validation
    if username in accounts_database and accounts_database[username] == encrypted_password:
        # Clear main window text fields before shifting focus
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        master_key_entry.delete(0, tk.END)
        
        # Proceed to separate file validation window
        open_key_verification_window(username)
    else:
        now = datetime.datetime.now()
        log_line = f"{now.strftime('%d-%m-%Y %H:%M:%S')} -> LOGIN FAILED (Primary Password Wrong) -> {username}"
        append_log_to_file(log_line)

        custom_message(
            "Login Failed",
            "Incorrect Username or Password",
            "#e74c3c",
            "#c0392b"
        )
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        master_key_entry.delete(0, tk.END)

def show_logs():
    log_window = tk.Toplevel(root)
    log_window.title("System Activity Logs")
    log_window.geometry("550x380")
    log_window.configure(bg="#f4f6f9")

    tk.Label(
        log_window,
        text="SYSTEM ACTIVITY LOGS",
        font=("Helvetica", 15, "bold"),
        bg="#f4f6f9",
        fg="#2c3e50"
    ).pack(pady=10)

    log_text = tk.Text(
        log_window,
        wrap=tk.WORD,
        width=60,
        height=15,
        font=("Courier New", 10),
        bg="white",
        fg="#2c3e50"
    )
    log_text.pack(padx=10, pady=10)

    if os.path.exists(LOGS_FILE):
        with open(LOGS_FILE, "r") as file:
            records = file.readlines()
    else:
        records = []

    if len(records) == 0:
        log_text.insert(tk.END, "No logs available.")
    else:
        for record in records:
            record = record.strip()
            if record:
                level = "WARNING" if "FAILED" in record else "INFO"
                log_text.insert(tk.END, f"{level} : {record}\n")

    log_text.config(state=tk.DISABLED)

    tk.Button(
        log_window,
        text="Close",
        command=log_window.destroy,
        bg="#e74c3c",
        fg="white",
        font=("Helvetica", 10, "bold"),
        padx=10,
        pady=5
    ).pack(pady=5)

# --- Main Window Setup ---

root = tk.Tk()
root.title("Cyber Security Portal")
root.geometry("420x520")
root.configure(bg="#f4f6f9")

title_label = tk.Label(
    root,
    text="CYBER SECURITY PORTAL",
    font=("Helvetica", 18, "bold"),
    bg="#f4f6f9",
    fg="#2c3e50"
)
title_label.pack(pady=25)

frame = tk.Frame(root, bg="#f4f6f9")
frame.pack(pady=10)

# Username Row
tk.Label(
    frame,
    text="Username:",
    font=("Helvetica", 11),
    bg="#f4f6f9",
    fg="#34495e"
).grid(row=0, column=0, sticky="w", pady=8)

username_entry = tk.Entry(
    frame,
    font=("Helvetica", 11),
    width=24
)
username_entry.grid(row=0, column=1, pady=8, padx=5)

# Password Row
tk.Label(
    frame,
    text="Password:",
    font=("Helvetica", 11),
    bg="#f4f6f9",
    fg="#34495e"
).grid(row=1, column=0, sticky="w", pady=8)

password_entry = tk.Entry(
    frame,
    font=("Helvetica", 11),
    width=24,
    show="*"
)
password_entry.grid(row=1, column=1, pady=8, padx=5)

# Secret Key Row (Required ONLY for Account Creation)
tk.Label(
    frame,
    text="Set Secret Key:",
    font=("Helvetica", 11),
    bg="#f4f6f9",
    fg="#34495e"
).grid(row=2, column=0, sticky="w", pady=8)

master_key_entry = tk.Entry(
    frame,
    font=("Helvetica", 11),
    width=24,
    show="*"
)
master_key_entry.grid(row=2, column=1, pady=8, padx=5)

button_style = {
    "font": ("Helvetica", 11, "bold"),
    "fg": "white",
    "width": 22,
    "pady": 7,
    "relief": "flat"
}

create_btn = tk.Button(
    root,
    text="Create Account",
    command=handle_create_account,
    bg="#2ecc71",
    **button_style
)
create_btn.pack(pady=8)

login_btn = tk.Button(
    root,
    text="User Login",
    command=handle_login,
    bg="#3498db",
    **button_style
)
login_btn.pack(pady=8)

logs_btn = tk.Button(
    root,
    text="View Activity Logs",
    command=show_logs,
    bg="#9b59b6",
    **button_style
)
logs_btn.pack(pady=8)

exit_btn = tk.Button(
    root,
    text="Exit Portal",
    command=root.quit,
    bg="#95a5a6",
    **button_style
)
exit_btn.pack(pady=20)

xroot.mainloop()