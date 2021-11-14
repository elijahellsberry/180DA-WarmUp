import socket

server_address = 'd4:3b:04:97:da:5f' # change this to your host device's mac address
port = 6

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect((server_address, port))
message = "I am CLIENT\n"
#client.sendto(message.encode(), (server_address, port))
client.send(bytes(message, 'UTF-8'))
data = client.recv(4096)
from_server = data.decode()
client.close()
print(from_server)
