import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hostname = '172.16.10.74'
port = 50007

message = input("-> ")
s.sendto(message.encode(),(hostname,port))



