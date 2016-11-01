import socket

server_address = ('127.0.0.1', 8000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.settimeout(1)
sock.connect((server_address))

try:
    echoMessage = "someMessage"
    message = "GET /server.php?message={} HTTP/1.1\n\n".format(echoMessage).encode()
    sock.send(message)

    data = b''

    while True:
        print("Entered loop")
        newData = sock.recv(4096)
        if newData:
            data += newData
        else:
            break

    print(data.decode("utf-8"))
finally:
    print("Closing Socket")
    sock.close()
