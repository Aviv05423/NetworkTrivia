import socket

SERVER_IP = "0.0.0.0"
PORT = 8821
MAX_MSF_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, PORT))
lop = 0
while lop == 0:
    (client_message, client_address) = server_socket.recvfrom(MAX_MSF_SIZE)
    data = client_message.decode()
    response = "Aviv's server say " + data
    server_socket.sendto(response.encode(), client_address)
    if data == "EXIT":
        lop = 1
        server_socket.close()
        break
    print("client send: " + data)

server_socket.close()
