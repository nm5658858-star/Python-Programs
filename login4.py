import hashlib
import datetime
import random
import tkinter as tk

# --- Data Storage ---
accounts = {}
activity_logs = []

def create_session():
    return random.randint(1000, 9999)

# --- Custom Stylish Message Box ---
def custom_message(title, message, bg_color, button_color):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("360x200")
    popup.configure(bg=bg_color)
    popup.resizable(False, False)

    # Title Label
    tk.Label(
        popup,
        text=title,
        font=("Helvetica", 15, "bold"),
        bg=bg_color,
        fg="white"
    ).pack(pady=15)

    # Message Label
    tk.Label(
        popup,
        text=message,
        font=("Helvetica", 11),
        bg=bg_color,
        fg="white",
        wraplength=300,
        justify="center"
    ).pack(pady=10)

    # OK Button
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

# --- GUI Functions ---

def handle_create_account():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        custom_message(
            "Warning",
            "Username and Password cannot be empty!",
            "#f39c12",
            "#d35400"
        )
        return

    if username in accounts:
        custom_message(
            "Error",
            "Username already exists!",
            "#e74c3c",
            "#c0392b"
        )
        return

    # Encrypt password using SHA-256
    encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    accounts[username] = encrypted_password

    now = datetime.datetime.now()

    activity_logs.append(
        f"{now.strftime('%d-%m-%Y %H:%M:%S')} -> ACCOUNT CREATED -> {username}"
    )

    custom_message(
        "Success",
        "Account Created Successfully!",
        "#2ecc71",
        "#27ae60"
    )

    # Clear Fields
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

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

    # Verify Login
    if username in accounts and accounts[username] == encrypted_password:

        session_id = create_session()
        login_time = datetime.datetime.now()

        activity_logs.append(
            f"{login_time.strftime('%d-%m-%Y %H:%M:%S')} -> LOGIN SUCCESS -> {username}"
        )

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

    else:
        activity_logs.append(
            f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> LOGIN FAILED -> {username}"
        )

        custom_message(
            "Login Failed",
            "Incorrect Username or Password",
            "#e74c3c",
            "#c0392b"
        )

    # Clear Fields
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def show_logs():

    # New Window for Logs
    log_window = tk.Toplevel(root)
    log_window.title("System Activity Logs")
    log_window.geometry("550x380")
    log_window.configure(bg="#f4f6f9")

    # Heading
    tk.Label(
        log_window,
        text="SYSTEM ACTIVITY LOGS",
        font=("Helvetica", 15, "bold"),
        bg="#f4f6f9",
        fg="#2c3e50"
    ).pack(pady=10)

    # Text Area
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

    if len(activity_logs) == 0:
        log_text.insert(tk.END, "No logs available.")
    else:
        for record in activity_logs:
            level = "WARNING" if "FAILED" in record else "INFO"
            log_text.insert(tk.END, f"{level} : {record}\n")

    log_text.config(state=tk.DISABLED)

    # Close Button
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

# --- Main Window ---

root = tk.Tk()
root.title("Cyber Security Portal")
root.geometry("420x470")
root.configure(bg="#f4f6f9")

# --- Title ---
title_label = tk.Label(
    root,
    text="CYBER SECURITY PORTAL",
    font=("Helvetica", 18, "bold"),
    bg="#f4f6f9",
    fg="#2c3e50"
)

title_label.pack(pady=25)

# --- Input Frame ---
frame = tk.Frame(root, bg="#f4f6f9")
frame.pack(pady=10)

# Username
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

# Password
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

# --- Button Styling ---
button_style = {
    "font": ("Helvetica", 11, "bold"),
    "fg": "white",
    "width": 22,
    "pady": 7,
    "relief": "flat"
}

# Create Account Button
create_btn = tk.Button(
    root,
    text="Create Account",
    command=handle_create_account,
    bg="#2ecc71",
    **button_style
)

create_btn.pack(pady=8)

# Login Button
login_btn = tk.Button(
    root,
    text="User Login",
    command=handle_login,
    bg="#3498db",
    **button_style
)

login_btn.pack(pady=8)

# View Logs Button
logs_btn = tk.Button(
    root,
    text="View Activity Logs",
    command=show_logs,
    bg="#9b59b6",
    **button_style
)

logs_btn.pack(pady=8)

# Exit Button
exit_btn = tk.Button(
    root,
    text="Exit Portal",
    command=root.quit,
    bg="#95a5a6",
    **button_style
)

exit_btn.pack(pady=20)

# --- Run Application ---
root.mainloop()