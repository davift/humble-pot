#!/usr/bin/python3
import socket
import threading

# Speficy the IP you want to bind on to avoid conflict the services running on the loopback interface.
BIND = '0.0.0.0'
# Single port (e.g. NFS)
PORTS = [2049]
# Multiple ports (e.g. SMB)
#PORTS = [445, 139]
# Range of ports (e.g. from 8080 to 8089, total of 10 ports)
#PORTS = [*range(8080, 8089 + 1)]

def listener(BIND, PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((BIND, PORT))
    server_socket.listen(1)
    print(" Listening on:", BIND, "port:", PORT, flush=True)

    try:
        while True:
            conn, address = server_socket.accept()
            print("from:", address[0], "on port:", PORT, flush=True)
            conn.close()
    except KeyboardInterrupt:
        print(' Interrupted', flush=True)
        conn.close()
        server_socket.close()
        exit()
    except:
        print('Potential portscan.', flush=True)

if __name__ == '__main__':
    threads = []
    for PORT in PORTS:
        thread = threading.Thread(target=listener, args=(BIND, PORT,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
