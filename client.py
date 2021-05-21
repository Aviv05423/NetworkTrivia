import socket
import chatlib  # To use chatlib functions or consts, use chatlib.****
import time

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678


# mark: HELPER SOCKET METHODS

def build_and_send_message(conn, code, data):
    """
    Builds a new message using chatlib, wanted code and message.
    Prints debug info, then sends it to the given socket.
    Paramaters: conn (socket object), code (str), data (str)
    Returns: Nothing
    """
    masg_send = chatlib.build_message(code, data)
    # print(masg_send)
    conn.send(masg_send.encode())


def recv_message_and_parse(conn):
    """
    Recieves a new message from given socket,
    then parses the message using chatlib.
    Paramaters: conn (socket object)
    Returns: cmd (str) and data (str) of the received message.
    If error occured, will return None, None
    """

    full_msg = conn.recv(1024).decode()
    cmd, data = chatlib.parse_message(full_msg)
    return cmd, data


def connect():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # my_socket.connect((IP, PORT))
    my_socket.connect((SERVER_IP, SERVER_PORT))
    print("connecting to " + str(SERVER_IP) + " port " + str(SERVER_PORT))
    return my_socket


def error_and_exit(error_msg):
    print(error_msg)
    exit()

def build_send_recv_parse(conn, code, data):
    build_and_send_message(conn, code, data)
    return recv_message_and_parse(conn)

# mark: The protocol

def login(conn):
    username = input("Please enter username: \n")
    password = input("Please enter password: \n")
    # username = "abc"
    # password = "123"
    user_pass = username + "#" + password
    login_success = False
    while login_success == False:
        build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"], user_pass)
        server_recv = recv_message_and_parse(conn)
        print(server_recv[1])
        # mseg = chatlib.parse_message(server_recv)
        if chatlib.PROTOCOL_SERVER["login_ok_msg"] in server_recv:
            print("Log in successfully!")
            return True
        else:
            print("Connection failed")
            return False


def logout(conn):
    build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["logout_msg"], "")
    conn.close()
    print("I closed the link with the server")


def get_score(conn):
    server_recv = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["score_msg"], "")
    print("your score is: " + server_recv[1])


def get_highscore(conn):
    server_recv = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["highscore_msg"], "")
    print("The highest score is: \n" + server_recv[1])


def play_question(conn):
    question = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["get_question"], "")
    if question[0] == "NO_QUESTIONS ":
        print("The server ran out of questions")
        return
    question_data = question[1].split("#")
    print(question_data[1])
    # print(question_data[2])

    user_question = input(" a): " + question_data[2] + "\n b): " + question_data[3] + "\n c): " + question_data[4] + "\n d): " + question_data[5] + "\n your answer: ")
    if "a" in user_question or "b" in user_question or "c" in user_question or "d" in user_question:
        pass
    else:
        print("Please choose from the options! (a / b / c / d)")
        user_question = input(
            " a): " + question_data[2] + "\n b): " + question_data[3] + "\n c): " + question_data[4] + "\n d): " +
            question_data[5] + "\n your answer: ")

    unsers = {"a": "1",
              "b": "2",
              "c": "3",
              "d": "4"
              }
    correct_answer = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["send_answer"], str(question_data[0]) + "#" + str(unsers[user_question]))
    if correct_answer[0] == "CORRECT_ANSWER":
        print("Well done correct answer!")
    elif correct_answer[0] == "WRONG_ANSWER":
        print("Wrong, the correct answer is: " + question_data[int(correct_answer[1]) + 1])
    else:
        error_and_exit("question_data")

def get_logged_users(conn):
    players_connected = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["players_connected"], "")
    players_connected_list = players_connected[1].split(",")
    players_connected_str = "Number of players connected: " + str(len(players_connected_list))
    for name in players_connected_list:
        players_connected_str += "\n" + name
    return players_connected_str




def main():
    my_socket = connect()
    if login(my_socket) == False:
        return
    print("\n")
    while True:
        user_input = input("""what would you like to do? \n p            Play a trivia question \n s            Get my score \n h            Get high score \n c            Get connected users \n q            Exit \n Please enter your choice: """)
        if user_input == "s":
            get_score(my_socket)
        elif user_input == "h":
            get_highscore(my_socket)
        elif user_input == "p":
            play_question(my_socket)
        elif user_input == "c":
            print(get_logged_users(my_socket))
        elif user_input == "q":
            logout(my_socket)
            return
        else:
            print(user_input + " is not option")
    # play_question(my_socket)
if __name__ == '__main__':
    main()
