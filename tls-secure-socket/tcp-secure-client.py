#handling errors in python socket programs

import socket   #for sockets
import sys  #for exit
import ssl


#create a default context
sslCtx = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)

try:
    #create an AF_INET, STREAM socket (TCP)
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Create a client side sslSocket
    tlsSocket = sslCtx.wrap_socket(socket, server_side=False, server_hostname ='www.google.com')
    print 'Secure Socket Created'
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()




remote_ip = "172.217.23.78"

#Connect to remote server
port = 443
tlsSocket.connect((remote_ip , port))

print 'Socket Connected to ' + remote_ip

#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try :
    #Set the whole string
    tlsSocket.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()

print 'Message send successfully'

#Now receive data
reply = tlsSocket.recv(4096)

print reply

tlsSocket.close()
