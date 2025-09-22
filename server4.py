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
            p=(h.decode("utf-8"))
            a=p[::-1]
            data = (a.encode("utf-8"))
            conn.sendall(data)
            
