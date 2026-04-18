import config

def login():
    print("=== Admin Login ===")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if not username or not password:
        print("Error: Username and password cannot be empty.")
        return

    if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD:
        print("Login successful!")
    else:
        print("Invalid credentials.")

def check_config():
    if not hasattr(config, 'ADMIN_USERNAME') or not hasattr(config, 'ADMIN_PASSWORD'):
        print("Error: Missing configuration values!")
        return False
    return True

if check_config():
    login()
else:
    print("Application cannot run due to missing configuration.")