import socket

server_address = 'd4:3b:04:97:da:5f' # change this to your host device's mac address
port = 0

# Initialization to add RFCOMM protocol to endpoint
serv = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Assigns a port for the server that listens to clients connecting to this port
serv.bind((server_address, port))
serv.listen(5)
while True:
    client, addr = serv.accept()
    from_client = ''
    while True:
        data = client.recv(4096)
        if not data: break 
        from_client = data.decode()
        #from_client += data
        print(from_client)
        message = "I am SERVER\n"
        client.sendto(message.encode(), (server_address, port))
    client.close()
    print('client disconnected')
