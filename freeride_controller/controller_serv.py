import socket
import json
import time

server_address = 'd4:3b:04:97:da:5f' 
port = 5

# Initialization to add RFCOMM protocol to endpoint
serv = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Assigns a port for the server that listens to clients connecting to this port
serv.bind(('d4:3b:04:97:da:5f', 5))
serv.listen()
prev_time = 0
while True:
    client, addr = serv.accept()
    while True:
        data = client.recv(4096)
        curr_time = time.time_ns()
        if not data: break 
        from_client_string = data.decode()
        from_client = json.loads(from_client_string)

        packet_time = (curr_time - prev_time) / (10**6)
        prev_time = curr_time

        print(str(packet_time) + " ms")




        # data = client.recv(4096)
        # curr_time = time.time_ns()
        # if not data: break
        # from_client = data.decode()
        # packet_time = (curr_time - prev_time) / (10**6)
        # prev_time = curr_time
        # print(str(packet_time) + "ms")





        #from_client += data
        #print(from_client)
        #message = "I am SERVER\n"
        #client.sendto(message.encode(), (server_address, port))
        #client.send(bytes(message, 'UTF-8'))
    client.close()
    print('client disconnected')
    break