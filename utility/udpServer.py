from socket import *
import utility.gvar as GV


def create_server_udp(plc, msg, com):
    plc_zona = GV.DB_PLCZONECONFIG.find_one({'name': plc})
    SERVER = GV.PLC_MASTER[:-3] + str(plc_zona['address'])
    ADDR = (SERVER, GV.PORT + int(plc_zona['address']))
    string_to_send = (str(com) + msg).encode(GV.FORMAT)
    buffer_length = len(string_to_send)
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.sendto(string_to_send, ADDR)
    msg_from_server = server_socket.recvfrom(buffer_length)
    server_socket.close()

    return msg_from_server
