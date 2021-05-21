import socket

SERVER_IP = "127.0.0.1"
PORT = 8821
MAX_MSG_SIZE = 1024

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


lop = 1
while lop == 1:
    user_input = input("What to send to Aviv's server? ")
    my_socket.sendto(user_input.encode(), (SERVER_IP, PORT))
    (response, remote_address) = my_socket.recvfrom(MAX_MSG_SIZE)
    data = response.decode()
    print("the server send: " + data)
    if user_input == "EXIT":
        lop = 0
        my_socket.close()
        break




my_socket.close()