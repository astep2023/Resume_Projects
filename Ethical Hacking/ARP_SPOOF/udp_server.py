import socket

server_ip:str = "10.0.0.2"
server_port:int = 25565
server:socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((server_ip, server_port))
print("UDP server is online on %i" % server_port)
while True:
    message, client_address = server.recvfrom(1024)
    print("'%s' sent from %s" % (client_address[0], message.decode()))
    server.sendto("Hello from Host 2".encode(), client_address)