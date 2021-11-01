#!/usr/bin/env python3

#version 1. Allows the first two clients that connect to send messages to each other indefinitely

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
#maximum backlog of connections set to 5
server.listen(5)

print("Listening on %s:%d" % (bind_ip, bind_port))

#modify to accept another client connection and pass data between the clients
def handle_client(client_socket):

	request = client_socket.recv(1024)
	print("[*] Received: %s" % request)

	while True:
		request = client_socket.recv(1024)
		client1.send(request)

while True:

	client1,addr1 = server.accept()
	client2,addr2 = server.accept()

	print("[*] Accepted connection from: %s:%d" % (addr1[0],addr1[1]))
	print("[*] Accepted connection from: %s:%d" % (addr2[0],addr2[1]))

	#client_handler = threading.Thread(target=handle_client,args=(client))
	#client_handler.start()

	while True:

		request = client1.recv(1024)
		print("Received: %s " % request)

		client2.send(request)

		request = client2.recv(1024)

		client1.send(request)

