import socket
def add():
    english_verb=input("please enter your english vord : ")
    pershian_verb=input("please enter mean vord :  ")
    s.sendall(english_verb.encode())
    s.sendall(pershian_verb.encode())
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1" , 60000))
    namber=0
    while True:
        name=input("please enter your add , dictionary , exit , serch or save : ")
        s.sendall(name.encode())
        if name=="add":
            add()
            namber=namber+1
        if name=="dictionary":
            for i in range (namber):
                key = s.recv(1024).decode()
                print(key)
                value = s.recv(1024).decode()
                print(f"mean:{value}")
                break
        elif name=="exit":
            s.close()
        elif name=="serch":
            masroche=input("please enter your vord : ")
            s.sendall(masroche.encode())
            finding= s.recv(1024).decode()
            if finding=="find": 
                key = s.recv(1024).decode()
                print(key)
                value1 = s.recv(1024).decode()
                print("mean:",value1)
            else:
                print("The word you searched for was not found.")
        elif name=="save":
            namefile=input("please enter your namm file : ")
            s.sendall(namefile.encode())
            print("ok :) Saved successfully")
        else:
            print("")