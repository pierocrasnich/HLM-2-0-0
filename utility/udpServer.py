import socket
import utility.gvar as GV


def create_server_udp(plc, msg, ms):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ADDR = (GV.PLC_MASTER, GV.PORT)
        string_to_send = (str(msg)).encode(GV.FORMAT)
        buffer_length = len(string_to_send)
        server_socket.sendto(string_to_send, ADDR)
        # msg_from_server = server_socket.recvfrom(buffer_length)
        server_socket.close()
        color = GV.RGBA_SUCCESS
        msg = "Download to PLC complete"
        ms.reg_console_msg(color, msg)
    except socket.error as msg:
        color = GV.RGBA_ERROR
        msg = str(msg)
        ms.reg_console_msg(color, msg)



