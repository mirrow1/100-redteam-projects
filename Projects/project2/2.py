#!/usr/bin/env python3

import socket

host,port = "127.0.0.1",9999
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((host,port))

clients = []

while True:

	message,addr = server.recvfrom(4096)

	if addr not in clients:
		clients.append(addr)

	for c in clients:
		if c != addr:
			sender = bytes("(" + addr[0] + "," + str(addr[1]) + ")# ","utf-8")
			server.sendto((sender+message),c)
