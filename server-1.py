import socket
HOST = '127.0.0.1' 
PORT = 60000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'server is listening on{HOST,PORT} ')
    conn, addr = s.accept() 
    with conn:
        print("Connected by", addr)
        while True:
            h = conn.recv(1024)
            print(h.decode("utf-8"))
            data = ('Hi from server!'.encode("utf-8"))
            conn.sendall(data)
            b = ('I got your message !'.encode("utf-8"))
            conn.sendall(b)
