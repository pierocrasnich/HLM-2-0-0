import utility.gvar as GV
from socket import *


def message_send(plc, com, msg):
    plc_zona = GV.DB_PLCZONECONFIG.find_one({'name': plc})
    sock = socket(AF_INET, SOCK_STREAM)
    address = GV.PLC_MASTER[:-3] + str(plc_zona['address'])
    server_address = (address, 10000)
    try:
        print('connecting to %s port %s' % server_address)
        sock.connect(server_address)
        # Send data
        print('sending "%s"' % msg)
        message = com + msg
        sock.sendall(message.encode())
        data = sock.recv(1024)
        print('Received: ', repr(data))
    except ConnectionRefusedError:
        print('Refuse Connection')
        sock.close()
    finally:
        print('closing socket')
        sock.close()