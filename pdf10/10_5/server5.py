import socket 
HOST= '127.0.0.1'
PORT=60000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("Server is listening on 127.0.0.1 , 60000")
    conn,addr= s.accept()
    print(f"Connected by {addr}")
    with conn:
        citys_informaition={"tehran":"25,sunny",
                            "mashhad" :"21,clouday",
                            "Tabriz":"-10,snowy"}
        while True:
            a= conn.recv(1024)
            a=a.decode()
            if a in citys_informaition:
                data= citys_informaition[a]
            else:
                data ="این شهر وجود ندارد "
            conn.sendall(data.encode())

     