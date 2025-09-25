import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 60000))
    a=input()
    h=(a.encode("utf-8"))
    s.sendall(h)
    data = s.recv(1024)
    print(data.decode("utf-8"))
     

#Client should get inputes into a While, 
#to receive multi-messages
#DO NOT FORGET "if not data: break" in all your socket programmings