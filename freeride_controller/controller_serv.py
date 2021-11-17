import socket
import json
import time

<<<<<<< HEAD
server_address = 'd4:3b:04:97:da:5f'
=======
server_address = 'd4:3b:04:97:da:5f' 
>>>>>>> ef8343cc19e2581fcec74078f27ef96dda8e18b5
port = 5

# Initialization to add RFCOMM protocol to endpoint
serv = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Assigns a port for the server that listens to clients connecting to this port
<<<<<<< HEAD
serv.bind(('5c:fb:3a:65:d7:80', 5))
serv.listen(5)
=======
serv.bind(('d4:3b:04:97:da:5f', 5))
serv.listen()
prev_time = 0
>>>>>>> ef8343cc19e2581fcec74078f27ef96dda8e18b5
while True:
    client, addr = serv.accept()
    while True:
        data = client.recv(4096)
<<<<<<< HEAD
        recv_time = time.time_ns()
        if not data: break
        from_client = data.decode()
        sent_time = int(from_client)
        #from_client_str = data.decode()
        #from_client = json.loads(data.decode())
        #sent_time = int(from_client["time"])
        latency = (recv_time - sent_time) / (10**6)
        print("Recieved at: " + str(recv_time) + " Transmit at: " + str(sent_time) + " Latency: " + str(latency))
=======
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




>>>>>>> ef8343cc19e2581fcec74078f27ef96dda8e18b5

        #from_client += data
        #print(from_client)
        #message = "I am SERVER\n"
        #client.sendto(message.encode(), (server_address, port))
        #client.send(bytes(message, 'UTF-8'))
    client.close()
    print('client disconnected')
    break