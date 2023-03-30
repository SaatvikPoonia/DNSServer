import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Prompt the user for the hostname to resolve
while True:
    hostname = input('Enter the hostname to resolve (q to quit): ')

    # Check if the user wants to quit
    if hostname.lower() == 'q':
        break

    # Send the DNS query to the server
    sock.sendto(hostname.encode(), ('localhost', 10000))

    # Receive the DNS response from the server
    response, addr = sock.recvfrom(1024)

    # Print the DNS response
    print(response.decode())

    # Prompt the user if they want to continue
    choice = input('Do you want to continue? (y/n): ')
    if choice.lower() == 'n':
        break

# Close the socket
sock.close()
