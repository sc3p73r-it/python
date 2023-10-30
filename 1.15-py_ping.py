from pythonping import ping 

address = input("Enter Server Address: ")
ping(address, verbose=True, count = 10)