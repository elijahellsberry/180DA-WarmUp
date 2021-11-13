import socket

server_address = "D4-3B-04-97-DA-5F"
port = 0


client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect((server_address, port))
message = "I am CLIENT\n"
client.sendto(message.encode(), (server_address, port))
data = client.recv(4096)
from_server = data.decode()
client.close()
print(from_server)
