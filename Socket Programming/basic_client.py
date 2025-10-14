import socket

#create connection
client = socket.socket()
client.connect(('127.0.0.1', 12345)) #IPv4 address, port number

#===== main body of program
#usually uses a while loop and an end condition to keep the socket connection open.

#=== send data
to_send=input()
client.sendall(to_send.encode('utf-8')) #this will ensure that all data is sent.

#=== receive data
received = b'' #b stands for bytes
while b'\n' not in received: #only print when all bytes are in (shown by the presence of the \n)
    received += client.recv(1024)
result=received.decode('utf-8')

#close connection
client.close()

#if u want to establish connection with a friend on the same network, change 127.0.0.1 to their IP