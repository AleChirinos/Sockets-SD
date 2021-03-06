import socket

host = socket.gethostname() 
port = 12345
BUFFER_SIZE = 1024 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:

    socket_tcp.bind((host, port)) 
    socket_tcp.listen(5)  
    conn, addr = socket_tcp.accept() 
    with conn:
        print('-> Conexión establecida') 
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            else:
                print('-> Datos recibidos: {}'.format(data.decode('utf-8'))) 
            conn.send(data) 