import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.224.76', 8080))
message = "I am CLIENT\n"
client.sendto(message.encode(), ('192.168.224.76', 8080))
data = client.recv(4096)
from_server = data.decode()
client.close()
print(from_server)
