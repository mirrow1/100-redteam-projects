Stolen from Black Hat Python

To start off, we pass in the IP address and port we want the server to listen on ➊. Next we tell the
server to start listening ➋ with a maximum backlog of connections set to 5. We then put the server
into its main loop, where it is waiting for an incoming connection. When a client connects ➍, we
receive the client socket into the client variable, and the remote connection details into the addr
variable. We then create a new thread object that points to our handle_client function, and we pass
it the client socket object as an argument. We then start the thread to handle the client connection ➎,
and our main server loop is ready to handle another incoming connection. The handle_client ➌
function performs the recv() and then sends a simple message back to the client.
