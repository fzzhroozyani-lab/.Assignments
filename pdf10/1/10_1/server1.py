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
            if a=="data":
                data=datetime.datetime.today().strftime("%Y-%m-%d")
            elif a=="time":
                data=datetime.datetime.now().strftime("%H:%M:%S")
            else :
                data='please enter a valid word'

            conn.sendall(data.encode())

#Good job!
#To make your code better:
#1.Choose meaningful words for variables.For example:
#'time' instead t,'date' instead d and...
#2.Use 'else' to make sure user won't enter an irrelevant word.
#if he'll do, program shows a nice answer. like 'please enter a valid word'
     