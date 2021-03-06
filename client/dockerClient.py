import socket

# Location of PHP server running in a docker container on Opennebula
server_address = ('10.62.0.174', 8000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.settimeout(1)

# Connect to the server
sock.connect((server_address))

try:
    # Build and send request
    echoMessage = "someMessage"
    message = "GET /server.php?message={} HTTP/1.1\n\n".format(echoMessage).encode()
    sock.send(message)

    data = b''

    # Loop until no more data is received
    while True:
        newData = sock.recv(4096)
        if newData:
            data += newData
        else:
            break

    # Print the result
    print(data.decode("utf-8"))
finally:
    sock.close()
