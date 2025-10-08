import socket 
import threading
HOST= '127.0.0.1'
PORT=60000
def connection():
    conn,addr= s.accept()
    with conn:
        #conn.sendall(b"Welcome! Type something:\n")
        while True:
            data= conn.recv(1024)
            print(f"message from {addr}: {data}")
            conn.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    while True:
        t=threading.Thread(target=connection)
        t.start()
        