import socket
import os

HOST = '127.0.0.1'
PORT = 8080


dic= {
    "{{name}}": "Student",
    "{{time}}": "now"  
}


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

def new_valu(nvalue):
    new_value = nvalue
    for key, value in dic.items():
        new_value = new_value.replace(key, value)
    return new_value

try:
    while True:
        client, addr = s.accept()
        request = client.recv(1024).decode('utf-8')

        try:
            enter = request.split(" ")[1]
        except IndexError:
            client.close()
            continue

        if enter == '/':
            enter = '/index.html'

        nenter = enter[1:]

        try:
            with open(nenter, 'r', encoding='utf-8') as f:
                html_valu = f.read()

            if nenter.endswith(".html"):
                end_value = new_valu(html_valu)
            else:
                end_value = html_valu

            body = end_value.encode('utf-8')

            response = b"HTTP/1.1 200 OK\r\n"

            if nenter.endswith(".html"):
                response += b"Content-Type: text/html; charset=utf-8\r\n"
            elif nenter.endswith(".css"):
                response += b"Content-Type: text/css\r\n"
            elif nenter.endswith(".js"):
                response += b"Content-Type: text/javascript\r\n"
            elif nenter.endswith(".jpg") or nenter.endswith(".jpeg"):
                response += b"Content-Type: image/jpeg\r\n"
            elif nenter.endswith(".png"):
                response += b"Content-Type: image/png\r\n"
            else:
                response += b"Content-Type: text/plain; charset=utf-8\r\n"

            response += b"Content-Length: " + str(len(body)).encode('utf-8') + b"\r\n"
            response += b"\r\n" + body

        except FileNotFoundError:
            response = b"HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>"
        except Exception as e:
            response = b"HTTP/1.1 500 Internal Server Error\r\n\r\n<h1>500 Internal Server Error</h1>"

        client.sendall(response)
        client.close()

except KeyboardInterrupt:
    print("end")
finally:
    s.close()