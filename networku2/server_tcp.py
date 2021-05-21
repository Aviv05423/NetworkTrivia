import random
from datetime import date
import socket
today = date.today()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((ip_address, 5050))
server_socket.listen()
print("server is run!")

(client_socket, client_address) = server_socket.accept()
print("client connected")

while True:
    data = client_socket.recv(1024).decode()
    print("client send: " + data)
    if data == "Quit":
        print("closing client socket now...")
        client_socket.send("Bye".encode())
        break
    elif data == "NAME":
        send_data = "Aviv's server"
    elif data == "TIME":
        d1 = today.strftime("%B %d, %Y")
        d2 = today.strftime("%d/%m/%Y")
        TIME = d1 + "\n" + d2
        send_data = TIME
    elif data == "RAND":
        send_data = str(random.randint(1, 10))

    else:
        send_data = data
    client_socket.send(send_data.encode())

client_socket.close()
server_socket.close()
