##http://www.cs.utexas.edu/~cannata/networking/Homework/WebServer.py
from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
host = '10.205.0.179'
serverPort = 60000
print 'hostname is: ', gethostname()
print 'Server ip is: ', host
serverSocket.bind((host, serverPort))
serverSocket.listen(1)
while True:
    print 'server is ready'
    (connectionSocket, addr) = serverSocket.accept()
    print ' connection received from: ', addr
    try:
        message = connectionSocket.recv(1024)
        print 'Message is: ', message
        filename = message.split()[1]
        print 'File name is: ', filename
        f = open(filename[1:], 'rb')
        data = f.readlines()
        connectionSocket.send('''HTTP/1.1 200 OK\r
\r
''')
        for i in range(0, len(data)):
            connectionSocket.send(data[i])
        connectionSocket.send('\r\n')
        connectionSocket.close()
    except IOError:
        connectionSocket.send('''HTTP/1.1 404 Not Found\r
\r
''')
        connectionSocket.send('<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n'
                              )
        connectionSocket.close()
serverSocket.close()

			
