import socket

s = socket.socket()
host = socket.gethostbyaddr('aws.ec2.public.ip')[0]
port = 12345

s.connect((host, port))
print(s.recv(1024).decode())
s.close()