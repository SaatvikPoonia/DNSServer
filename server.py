import socket

# DNS table containing hostname to IP mappings and aliases
dns_table = {
    'www.example.com': {'type': 'A', 'value': '192.168.0.1'},
    'example.com': {'type': 'CNAME', 'value': 'www.example.com'},
    'www.google.com': {'type': 'A', 'value': '8.8.8.8'},
    'google.com': {'type': 'CNAME', 'value': 'www.google.com'}
}

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 10000)
sock.bind(server_address)

print('DNS server is up and running.')

while True:
    # Receive a DNS query from the client
    query, addr = sock.recvfrom(1024)

    # Decode the query from bytes to string
    hostname = query.decode().strip()

    # Check if the hostname is in the DNS table
    if hostname in dns_table:
        response_type = dns_table[hostname]['type']
        response_value = dns_table[hostname]['value']

        # Construct the DNS response message
        response = f'{hostname} has {response_type} record ' \
                   f'value: {response_value}'.encode()
    else:
        # Construct an error message for an unknown hostname
        response = f'Error: Hostname {hostname} not found ' \
                   f'\n ip_address = "0.0.0.0" '.encode()

    # Send the DNS response to the client
    sock.sendto(response, addr)
