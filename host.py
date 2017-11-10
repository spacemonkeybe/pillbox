from socket import *
import os
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer

#
# http server: commuicate with doctor's client
#
def httpserver():
	Protocol     = "HTTP/1.0"
	port = 8000
	server_address = ('127.0.0.1', port)
	HandlerClass.protocol_version = Protocol
	httpd = ServerClass(server_address, HandlerClass)
	sa = httpd.socket.getsockname()
	print "Serving HTTP on", sa[0], "port", sa[1], "..."
	httpd.serve_forever()

#
#pill box server: get info and send order to pill box
#
def pillboxserver():
	HOST = ''
	PORT = 21567
	BUFSIZ = 1024
	ADDR = (HOST,PORT)

	tcpSerSock = socket(AF_INET, SOCK_STREAM)
	tcpSerSock.bind(ADDR)
	tcpSerSock.listen(5)
	while True:
		print 'waiting for connection...'
		tcpCliSock,addr = tcpSerSock.accept()
		print '...connected from: ',addr

		while True:
		    data = tcpCliSock.recv(BUFSIZ)
		    if not data:
		        break
		    print "="*20
		    print "[From Client]:",data
		    message = raw_input("Service>")
		    tcpCliSock.send(message)
	tcpSerSock.close()

#
# main control: create two process pillboxserver and httpserver
#

pid = os.fork()
if pid == 0:
	print 'init http server'
	httpserver()
else:
    print 'init pillbox server'
    pillboxserver()

