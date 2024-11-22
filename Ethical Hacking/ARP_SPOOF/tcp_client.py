import socket

client:socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.0.0.1', 8080)) 

while True:
    message:str = input("Enter message to send: ")
    client.sendall(message.encode())
    contents = client.recv(1024)
    print("%s" % contents.decode())