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
sock.bind(server_address)
print(' Listening on:', BIND, "port:", PORT, flush=True)

try:
    while True:
        data, address = sock.recvfrom(4096)
        #print('Data: {!r}'.format(data), flush=True)

        # Parse the incoming DNS request
        transaction_id = data[:2]
        received_domain_name = data[12:-27]
        domain = received_domain_name[1:-1].decode('utf-8').translate(str.maketrans(dict.fromkeys(range(0x00, 0x20), '.')))
        if str(domain) == '':
            domain = 'PORTSCAN'
        ip_address = "1.2.3.4"
        ip_in_bytes = bytes([int(x) for x in ip_address.split(".")])

        # Construct the response
        response = transaction_id + b'\x81\x80\x00\x01\x00\x01\x00\x00\x00\x01' + received_domain_name + b'\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00\x00\x38\x00\x04' + ip_in_bytes

        print('from: {} on port: {} bytes: {} domain: {}'.format(address[0], PORT, len(data), domain), flush=True)
        sent = sock.sendto(response, address)
        #print('Sent {} bytes back to {}'.format(sent, address[0]), flush=True)
except KeyboardInterrupt:
    print(' Interrupted', flush=True)
    exit()
