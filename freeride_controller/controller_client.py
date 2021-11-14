import bluetooth

server_address = 'd4:3b:04:97:da:5f'
port = 6


#client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
client.connect((server_address, port))
message = "I am CLIENT\n"
client.send(message)
#client.sendto(message.encode(), (server_address, port))
data = client.recv(4096)
from_server = data.decode()
client.close()
print(from_server)
