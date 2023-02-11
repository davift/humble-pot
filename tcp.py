#!/usr/bin/python3
import socket
import threading

def listener(PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', PORT))
    server_socket.listen(1)
    print("Honeypot listening on port", PORT)

    try:
        while True:
            conn, address = server_socket.accept()
            print("Received connection from", address[0], "on port", PORT)
            conn.close()
    except KeyboardInterrupt:
        print(' Interrupted')
        conn.close()
        server_socket.close()
        exit()

if __name__ == '__main__':
    # Single port (e.g. NFS)
    ports = [2049]
    # Multiple ports (e.g. SMB)
    #ports = [445, 139]
    # Range of ports (e.g. from 8080 to 8089, total of 10 ports)
    #ports = [*range(8080, 8089 + 1)]

    threads = []
    for port in ports:
        thread = threading.Thread(target=listener, args=(port,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
        exit()
