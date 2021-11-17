import socket
import json
import time

server_address = 'd4:3b:04:97:da:5f'
port = 5

# Initialization to add RFCOMM protocol to endpoint
serv = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Assigns a port for the server that listens to clients connecting to this port
serv.bind(('5c:fb:3a:65:d7:80', 5))
serv.listen(5)
while True:
    client, addr = serv.accept()
    from_client = ''
    while True:
        data = client.recv(4096)
        recv_time = time.time_ns()
        if not data: break
        from_client = data.decode()
        sent_time = int(from_client)
        #from_client_str = data.decode()
        #from_client = json.loads(data.decode())
        #sent_time = int(from_client["time"])
        latency = (recv_time - sent_time) / (10**6)
        print("Recieved at: " + str(recv_time) + " Transmit at: " + str(sent_time) + " Latency: " + str(latency))

        #from_client += data
        #print(from_client)
        #message = "I am SERVER\n"
        #client.sendto(message.encode(), (server_address, port))
        #client.send(bytes(message, 'UTF-8'))
    client.close()
    print('client disconnected')
    break