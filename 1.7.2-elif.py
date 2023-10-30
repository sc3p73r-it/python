username = input("Enter Username :")
allow_user = ["admin","root","dream"]
if username in allow_user:
    print("Welcom Back",username)

elif username not in allow_user:
    print("Wrong Username!")