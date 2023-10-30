import socket

host = "192.168.43.47"
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print (s.recv(1024).decode())
s.close()

