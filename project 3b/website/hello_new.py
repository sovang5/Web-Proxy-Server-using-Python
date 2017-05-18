
## http://stackoverflow.com/questions/30109605/http-proxy-server-python
from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
host = '10.205.0.179'
serverPort = 60000

print 'hostname is: ',gethostname()
print 'Server ip is: ', host
serverSocket.bind((host, serverPort))
serverSocket.listen(1)
while True:
    print 'Server is Ready...'
    (connectionSocket, addr) = serverSocket.accept()
    print ' connection received from: ', addr
    try:

        message = connectionSocket.recv(1024)
        print 'Message is: ', message
        filename = message.split()[1]
        print 'File name is: ', filename
        try:
            f = open(filename[1:],'rb')
            outputdata = f.readlines()
            print "file found"
            connectionSocket.send('''HTTP/1.1 200 OK\r\n\r\n''')
            for i in range(0, len(data)):
                connectionSocket.send(data[i])
            connectionSocket.send('\r\n')
            connectionSocket.close()
        except:
            serverProxy = socket(AF_INET,SOCK_STREAM)
            
            print "before web"
            web=filename[1:]
            print web
            try:
                print "file is not present in server cache\n cacheing....."
                serverProxy.connect((web, 80))

                print 'Socket connected to port 80 of the host'
                print '301 MOved permanently'
                fileobj = serverProxy.makefile('r', 0)
                fileobj.write("GET "  +"http://"+ web + " HTTP/1.0\n\n")
                buffer = fileobj.readlines()
                tmp_File = open("./" + web, "wb")
                for i in range(0, len(buffer)):
                    tmp_File.write(buffer[i])
                    connectionSocket.send(buffer[i])
                connectionSocket.close()
            except IOError:
                print 'Illegal Request'
                connectionSocket.send('''HTTP/1.1 404 Not Found\r\n\r\n''')
                connectionSocket.send('<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n')
                connectionSocket.close()
    except IOError:
        print 'Read Message Error'
serverSocket.close()
