#192.168.1.27
import socket
import pickle

HOST = '192.168.1.28'  # Standard loopback interface address (localhost)
PORT = 5678        # Port to listen on (non-privileged ports are > 1023)

#print(HOST)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)


clientsocket, address = s.accept()
print(f"Connection from {address} has been established!")
clientsocket.close()