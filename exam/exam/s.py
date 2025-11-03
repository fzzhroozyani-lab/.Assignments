import socket 
import threading
def connection(conn,addr):
    print(f"connection from{addr}")
    with conn:
        dic={}
        while True:
            try:
                data = conn.recv(1024).decode('utf-8')
                if data=="add":
                    english_verb = conn.recv(1024).decode('utf-8')
                    pershian_verb = conn.recv(1024).decode('utf-8')
                    dic[english_verb] = pershian_verb
                if data=="dictionary":
                    number=str(len(dic))
                    for i in dic:
                        conn.sendall(i.encode())
                        conn.sendall(dic[i].encode())
                if data=="serch":
                    masroch=conn.recv(1024).decode('utf-8')
                    for i in dic:
                        if masroch==i:
                            eror1="find"
                            conn.sendall(eror1.encode())
                            conn.sendall(i.encode())
                            conn.sendall(dic[i].encode())
                if data =="save":
                    name_file=conn.recv(1024).decode('utf-8')                    
                    file=open(f'{name_file}.txt','w')
                    for i in dic:
                        file.write(i) 
                        file.write(dic[i])
                    file.close
            except:
                break
def main():
    HOST= '127.0.0.1'
    PORT=60000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        while True:
            conn,addr= s.accept()
            t=threading.Thread(target=connection,args=(conn,addr))
            t.start()
main()