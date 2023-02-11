#!/usr/bin/python3
import socket
import base64

# Specify the IP you want to bind on.
BIND = '0.0.0.0'
# To listen on the default port 80 might require root privileges.
PORT = 80

def listener(BIND, PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((BIND, PORT))
    server_socket.listen(1)

    while True:
        try:
            conn, address = server_socket.accept()
            data = conn.recv(1024).decode()
            if data.startswith("GET"):
                conn.send("HTTP/1.1 401 Unauthorized\r\n".encode())
                auth = None
                for header in data.split("\r\n"):
                    if header.startswith("Authorization: Basic"):
                        auth = header.split(" ")[-1]
                        break
                if auth:
                    auth = base64.b64decode(auth).decode().split(":")
                    print("Connection from:", address[0], "on port:", PORT, "username:", auth[0], "password:", auth[1])
                else:
                    print("Connection from:", address[0], "on port:", PORT)
                conn.send("WWW-Authenticate: Basic realm=\"Authentication Required\"\r\n".encode())
            conn.close()
        except KeyboardInterrupt:
            print('Interrupted')
            conn.close()
            server_socket.close()
            exit()
        except:
            print("Connection from:", address[0], "on port:", PORT, 'error: PORTSCAN')

if __name__ == '__main__':
    print("Listening on", BIND, "port", PORT)
    while True:
        listener(BIND, PORT)

exit()
