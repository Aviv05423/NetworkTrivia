# Protocol Constants
import functools

CMD_FIELD_LENGTH = 16  # Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4  # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10 ** LENGTH_FIELD_LENGTH - 1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages 
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
    "login_msg": "LOGIN",
    "logout_msg": "LOGOUT",
    "score_msg": "MY_SCORE",
    "highscore_msg": "HIGHSCORE",
    "get_question": "GET_QUESTION",
    "send_answer": "SEND_ANSWER",
    "players_connected": "LOGGED"
}  # .. Add more commands if needed

PROTOCOL_SERVER = {
    "login_ok_msg": "LOGIN_OK",
    "login_failed_msg": "ERROR",
    "user_score": "YOUR_SCORE",
    "all_score": "All_SCORE"
}  # ..  Add more commands if needed

# Other constants

ERROR_RETURN = None  # What is returned in case of an error


def build_message(cmd, data):
    """
    Gets command name (str) and data field (str) and creates a valid protocol message
    Returns: str, or None if error occured
    """
    if len(cmd) <= CMD_FIELD_LENGTH and len(data) <= MAX_DATA_LENGTH:
        for num in range(CMD_FIELD_LENGTH):
            if len(cmd) <= CMD_FIELD_LENGTH - 1:
                cmd = cmd + " "
        final_message = cmd + DELIMITER + f'{len(data):04}' + DELIMITER + data
        return final_message

    else:
        return ERROR_RETURN


def parse_message(data):
    """
    Parses protocol message and returns command name and data field
    Returns: cmd (str), data (str). If some error occured, returns None, None
    """
    data_list = data.split("|")
    try:
        int(data_list[1].replace(" ", "").replace("0", ""))
        if len(data_list) != 3 or len(data_list[0]) > CMD_FIELD_LENGTH or len(data_list[1]) > 4 or len(
                data_list[2]) != int(data_list[1]):
            return ERROR_RETURN, ERROR_RETURN
    except:
        if data_list[1].replace(" ", "").replace("0", "") == "":
            pass
        else:
            return ERROR_RETURN, ERROR_RETURN

    cmd = data_list[0].replace(" ", "")
    msg = data_list[2]
    return cmd, msg


def split_data(msg, expected_fields):
    """
    Helper method. gets a string and number of expected fields in it. Splits the string
    using protocol's data field delimiter (|#) and validates that there are correct number of fields.
    Returns: list of fields if all ok. If some error occured, returns None
    """
    returnList = msg.split(DATA_DELIMITER)
    if len(returnList) == expected_fields:
        return returnList
    # print(returnList)
    else:
        returnList = [ERROR_RETURN]
        return returnList
    # print(returnList)


def join_data(msg_fields):
    """
    Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter.
    Returns: string that looks like cell1#cell2#cell3
    """
    combine = functools.reduce(lambda x, y: str(x) + DATA_DELIMITER + str(y), msg_fields)
    return combine
