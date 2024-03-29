#!/usr/bin/python3
import socket

# Specify the IP you want to bind on.
BIND = '0.0.0.0'
# To listen on the default port 21 might require root privileges.
PORT = 21

def listener(BIND, PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((BIND, PORT))
    server_socket.listen(1)
    print(" Listening on:", BIND, "port:", PORT, flush=True)

    while True:
        try:
            conn, address = server_socket.accept()
            conn.send("220 (vsFTPd 3.0.3)\r\n".encode())
            username = conn.recv(1024).decode().strip()
            if username.startswith("USER"):
                username = username.split(" ")[1]
                conn.send("331 Please specify the password.\r\n".encode())
                password = conn.recv(1024).decode().strip()
                if password.startswith("PASS"):
                    password = password.split(" ")[1]
                    conn.send("530 Login incorrect.\r\n".encode())
                print("from:", address[0], "on port:", PORT, "username:", username, "password:", password, flush=True)
            else:
                print("from:", address[0], "on port:", PORT, flush=True)
            conn.close()
        except KeyboardInterrupt:
            print(' Interrupted', flush=True)
            conn.close()
            server_socket.close()
            exit()
        except:
            print("from:", address[0], "on port:", PORT, "error: PORTSCAN", flush=True)

if __name__ == '__main__':
    listener(BIND, PORT)

exit()
