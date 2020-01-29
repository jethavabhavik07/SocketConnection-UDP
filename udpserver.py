import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

hostname = '172.16.10.120'
port = 1234

s.bind((hostname,port))

while True:
	data,address = s.recvfrom(1024)
	print("Message Received : " + data.decode())
	