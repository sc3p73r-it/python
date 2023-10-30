import socket
host ="192.168.43.98"
port = 22222

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(3)
print("Waiting for imconfig connection with Port:",port)

while True:
    conn, addr = s.accept()
    print("Got connection from",addr)
    message= "Hi This is an server"
    conn.send(message.encode())
    conn.close()