#
# CPSC-471 Assignment 1
# Name: Nhat Nguyen
# CWID: 889090841
# Add various socket calls in various places, as required.
# Just a hint, see the sample TCPServer.py in the book
#
# Disclaimer:  There are no guarantees that the comments or
#              the code in this file are very accurate
#

#import socket module
from socket import *
import sys                       # In order to terminate the program

# Create a TCP server socket
# AF_INET is used for IPv4 protocols
# SOCK_STREAM is used for TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverHost = 'localHost'

# use port 80 for HTTP
serverPort = 2407

# associate the server port number with this socket
serverSocket.bind(('', serverPort))

# wait and listen for some client to knock on the door
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        print(message, '::', message.split()[0], ':', message.split()[1])

        filename = message.split()[1]
        f = open(filename[1:])

        # read the file and store the content in the outputdata
        outputdata = f.read()
        # print out the content of the output data.
        print(outputdata)

        # Send one HTTP header line into socket
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\n\n'.encode())

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()

sys.exit()  # Terminate the program after sending the corresponding data

