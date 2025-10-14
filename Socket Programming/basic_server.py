import socket
import time

#server selects a port and waits there for a client to connect
server = socket.socket()
server.bind(('127.0.0.1', 12345))
server.listen() #indefinite waiting

#server has found a friend, yippee
#server accepts the client's connection and they move to a new port (addr) together
server_new, addr = server.accept()
print('Connected to: ' + str(addr))

#
# main body, send and receive works exactly the same as the client. see client for send/recv example.
#

#close both
server_new.close()
server.close()

#if you want to allow connection from another laptop, use 0.0.0.0 to allow all connections. 127.0.0.1 accepts only self, and <your IP addr> accepts others on same network, but not self. *firewall instructions not included.