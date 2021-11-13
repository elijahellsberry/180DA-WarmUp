import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = bluetooth.PORT_ANY # due to deprecated fn get_available_ports
#uuid = uuid.uuid4()
#uuid = str(uuid)
uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"

#port = bluetooth._get_available_ports(bluetooth.RFCOMM)

server_sock.bind(("",port))
server_sock.listen(1)
print("listening on port " + str(port))

bluetooth.advertise_service(server_sock, "Freeride game service", uuid)

client_sock, address = server_sock.accept()
print("accepted connection from: ", address)

data = client_sock.recv(1024)
print("received [%s]", data)

client_sock.close()
server_sock.close()