import socket
import sys
import ssl

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port


#create a default context
sslCtx = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'




try:
    #create secure socket and bind it
    tlsSocket = sslCtx.wrap_socket(socket, server_side=True)
    tlsSocket.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Secure Socket bind complete'

tlsSocket.listen(10)
print 'Secure Socket now listening'

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = tlsSocket.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    data = conn.recv(1024)
    reply = 'OK...' + data
    if not data or data.rstrip() == "ciao":
        break

    conn.sendall(reply)

    conn.close()

tlsSocket.close()
