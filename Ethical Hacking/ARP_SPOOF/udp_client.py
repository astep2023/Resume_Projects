import socket

server_ip:str = "10.0.0.2"
server_port:int = 25565

client:socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Sending to %s:%i" % (server_ip, server_port))
client.sendto("Hello from Host 1".encode(), (server_ip, server_port))

response, server_address = client.recvfrom(1024)
print("%s sent %s" % (server_address[0], response.decode()))


