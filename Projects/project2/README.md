<h2>Project 2 - UDP chat server</h2>

In Project 1 I created a TCP chat server which allowed two connecting clients to send data between each other.
For this project's UDP chat server, I wanted to create a chat server in the way I think it was meant to be interpreted, that is, one that broadcasts messages from clients to everyone in the chat room.

There were a few things I learnt here, such as the fact I can't use socket.socket's listen() or accept() functions because the server is UDP (duh). I can simply receive the data.
I was reminded that data sent over the socket had to be encoded as bytes when I wanted to send the IP address and port received from the recvfrom() function.

In order to allow the data to be broadcast to all clients, I created a list ("clients") which tracked the IP addresses and ports from clients as they sent a message to the server. Because of this, clients that had only connected but not sent any data were not added to the list and unable to receive messages until they sent one.

The message being sent was also being returned to the sender as they were in the "clients" list. I added an if loop to check if the data sender matched the client in the clients list, if it did then the message won't be sent to that client.

How to use it:

start the server, then connect to it with a client using "nc -u 127.0.0.1 9999"

-u means send a UDP packet. It's connectionless so killing the server doesn't close the nc session. You can use it to type messages, and each message will be sent as UDP packets
