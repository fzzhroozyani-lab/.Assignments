import socket 
import datetime
HOST= '127.0.0.1'
PORT=60000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("Server is listening on 127.0.0.1 , 60000")
    conn,addr= s.accept()
    print(f"Connected by {addr}")
    with conn:
        while True:
            a= conn.recv(1024)
            a=a.decode()
            if a== "exit" :
                break
            elif a=="hello":
                data="hi"
            elif a=="by":
                data="goodby"
            conn.sendall(data.encode())
            

#your file didn't have right file extention: .py
#please read Question2 again.