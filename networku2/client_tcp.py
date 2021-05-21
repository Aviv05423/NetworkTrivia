import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# my_socket.connect((IP, PORT))
# my_socket.connect(("127.0.0.1", 8822))
my_socket.connect(("172.31.6.11", 22))
# my_socket.connect(("ec2-18-222-216-47.us-east-2.compute.amazonaws.com", 22))


data = ""
while data != "Bye":
    msg = input("what send to server?\n(NAME / TIME / RAND)\n")
    my_socket.send(msg.encode())
    data = my_socket.recv(1024).decode()
    print("server send: " + data)

my_socket.close()

