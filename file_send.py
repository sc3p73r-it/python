import socket
s = socket.socket()
host = "192.168.100.111"
port = 4444
s.bind((host, port))
s.listen(1)
print("Waiting for any incoming connection",port)
conn, addr = s.accept()
print(addr,"Has connected to the server")

#File Transfer

filename = input("Enter File Name: ")
files = open(filename, 'rb')
file_data = files.read(1024)
conn.send(file_data)
print("File Transfer Has been success")