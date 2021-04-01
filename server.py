import socket
# summary: creating a TCP server

# socket type and family specified here /creating socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)


host = socket.gethostname()  # gets host name
port = 4444

# bind host and port to socket
# host will be replaced/subsituted with ip, if changed and not running on host
serversocket.bind((host, port))

# listen to connect up to 3/ starts ip listener
serversocket.listen(3)

# while all of that is true
while True:
    clientsocket, address = serversocket.accept()

    # concat the address on to the output
    print ("Recieved connection from %s " % str(address))

    message = "Thank you for connecting to the server" + "\r\n"

    # sends message to client once they connect to the server
    clientsocket.send(message.encode('ascii'))
    # close the socket
    clientsocket.close()
