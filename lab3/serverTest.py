import socket
# Initialization to add TCP/IP protocol to the endpoint
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assigns a port for the server that listens to clients connecting to this port
serv.bind(('127.0.0.1', 8080))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break 
        from_client = data.decode()
        #from_client += data
        print(from_client)
        message = "I am SERVER"
        conn.sendto(message.encode(), ('127.0.0.1', 8080))
    conn.close()
    print('client disconnected')
