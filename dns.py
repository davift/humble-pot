#!/usr/bin/python3
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Speficy the IP you want to bind on to avoid conflict the services running on the loopback interface.
BIND = '0.0.0.0'
# To listen on the default port 53 it might require root privileges.
PORT = 53

# Bind the socket to a specific address and port
server_address = (BIND, PORT)
print('Starting up on {}:{}'.format(*server_address))
sock.bind(server_address)

try:
    while True:
        data, address = sock.recvfrom(4096)
        print('Received {} bytes from {} on port {}.'.format(len(data), address[0], PORT))
        #print('Data: {!r}'.format(data))

        # Parse the incoming DNS request
        transaction_id = data[:2]
        received_domain_name = data[12:-27]
        ip_address = "1.2.3.4"
        ip_in_bytes = bytes([int(x) for x in ip_address.split(".")])

        # Construct the response
        response = transaction_id + b'\x81\x80\x00\x01\x00\x01\x00\x00\x00\x01' + received_domain_name + b'\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00\x00\x38\x00\x04' + ip_in_bytes

        sent = sock.sendto(response, address)
        #print('Sent {} bytes back to {}'.format(sent, address[0]))
except KeyboardInterrupt:
    print(' Interrupted')
    exit()
