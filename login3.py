import hashlib
import datetime
import random
# Store users
accounts = {}
# Activity history
activity_logs = []
# Generate Session ID
def create_session():
    return random.randint(1000, 9999)
while True:
    print("\n====== CYBER SECURITY PORTAL ======")
    print("1. Create Account")
    print("2. User Login")
    print("3. View Activity Logs")
    print("4. Exit")
    option = input("Select Option: ")
    # CREATE ACCOUNT
    if option == "1":
        username = input("Create Username: ")
        if username in accounts:
            print("Username already exists!")
            continue
        password = input("Create Password: ")
        # Encrypt password
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        accounts[username] = encrypted_password
        now = datetime.datetime.now()
        activity_logs.append(
            f"{now.strftime('%d-%m-%Y %H:%M:%S')} -> ACCOUNT CREATED -> {username}"
        )
        print("Account Created Successfully")
    # USER LOGIN
    elif option == "2":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        # Verify login
        if username in accounts and accounts[username] == encrypted_password:
            session_id = create_session()
            login_time = datetime.datetime.now()
            activity_logs.append(
                f"{login_time.strftime('%d-%m-%Y %H:%M:%S')} -> LOGIN SUCCESS -> {username}"
            )
            print("\nLogin Successful")
            print("Welcome:", username)
            print("Session ID:", session_id)
            print("Login Time:", login_time.strftime("%H:%M:%S"))
        else:
            activity_logs.append(
                f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> LOGIN FAILED -> {username}"
            )
            print("Incorrect Username or Password")
    # VIEW LOGS
    elif option == "3":
        print("\n====== SYSTEM ACTIVITY LOGS ======")
        if len(activity_logs) == 0:
            print("No logs available")
        else:
            for record in activity_logs:
                if "FAILED" in record:
                    level = "WARNING"
                else:
                    level = "INFO"
                print(f"{level} : {record}")
    # EXIT
    elif option == "4":
        print("Closing Security Portal...")
        print("Portal Closed!")
        break
    # INVALID OPTION
    else:
        print("Invalid Selection")