import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
message = "I am CLIENT\n"
client.sendto(message.encode(), ('127.0.0.1', 8080))
data = client.recv(4096)
from_server = data.decode()
client.close()
print(from_server)
