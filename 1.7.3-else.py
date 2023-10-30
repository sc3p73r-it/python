username = input("Enter Username :")
password = input("Enter Password :")

if (username,password) == ("admin","123456"):
    print ("Welcome Back",username)

elif (username) != "admin":
    print("Wrong Username")

else:
    print("Wrong Password")