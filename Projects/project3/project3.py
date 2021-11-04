#!/usr/bin/env python3

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
#maximum backlog of connections set to 5
server.listen(5)

print("Listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket, clients):

	clients.append(client_socket)
	client_socket.send(b"Please state name: ")
	displayname = client_socket.recv(1024)
	client_socket.send(b"Welcome to the chat room, " + displayname)

	while True:

		request = client_socket.recv(1024)
		print("[*] Received: %s" % str(request))

		disp = str(displayname)
		disp = disp.replace("b'","")
		disp = disp.replace("\\n'","")
		message = bytes(disp,"utf-8") + b"# " + request

		for c in clients:
			if client_socket != c:
				#c.send(bytes(message,"utf-8"))
				c.send(message)

clients = []

while True:

	client,addr = server.accept()

	print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))

	client_handler = threading.Thread(target=handle_client,args=(client, clients))
	client_handler.start()
