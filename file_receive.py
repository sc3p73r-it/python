import socket

s = socket.socket()
host = "192.168.100.1111"
port = 4444
s.connect((host,port))
print("Connected...")


#File Receive
file = open("receive","wb")
file_data = s.recv(1024)
file.write(file_data)
file.close()

print("File Has been received")
