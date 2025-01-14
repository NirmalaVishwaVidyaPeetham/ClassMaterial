# Login System:
# Scenario: Imagine building a website's login system. You need to check if the entered username and password match the stored credentials.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "Sadashiva" and password == "123abc":
    print("Login successful!")
else:
    print("Invalid username or password.")