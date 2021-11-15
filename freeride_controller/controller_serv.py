import socket
import json
import time

server_address = 'd4:3b:04:97:da:5f'
port = 5

# Initialization to add RFCOMM protocol to endpoint
serv = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Assigns a port for the server that listens to clients connecting to this port
serv.bind((server_address, port))
serv.listen(1)
while True:
    client, addr = serv.accept()
    from_client = ''
    while True:
        data = client.recv(4096)
        if not data: break 
        from_client_string = data.decode()
        print(type(from_client_string))
        from_client = json.load(from_client_string)
        recv_time = time.time_ns()
        sent_time = int(from_client["time"])
        latency = recv_time - sent_time
        print(str(latency) + " ms")

        #from_client += data
        #print(from_client)
        #message = "I am SERVER\n"
        #client.sendto(message.encode(), (server_address, port))
        #client.send(bytes(message, 'UTF-8'))
    client.close()
    print('client disconnected')
    break

