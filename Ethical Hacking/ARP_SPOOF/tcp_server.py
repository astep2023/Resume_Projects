import socket

server:socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('10.0.0.1', 8080)) 
server.listen(1)
print("Server is listening...")

connection, addr = server.accept()
print("Connection from %s:%s" % (addr[0], addr[1]))

while True:
    contents = connection.recv(1024)
    print("%s" % contents.decode())
    connection.sendall("Message received!".encode())

