import utility.gvar as GV
import socket
import threading
from kivy.clock import Clock
import time


def create_server(plc, msg, com, start):
    plc_zona = GV.DB_PLCZONECONFIG.find_one({'name': plc})
    GV.SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = ("", GV.PORT + int(plc_zona['address']))
    GV.COMMAND = str(com) + msg
    if start:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.setblocking(False)
        print('# Socket created')
        server.bind(ADDR)

        def handle_client(conn, addr):
            print(f"[NEW CONNECTION] {addr} connected!")
            connect = True
            while connect:
                conn.send(GV.COMMAND)
                msg_length = conn.recv(GV.HEADER).decode(GV.FORMAT)
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(GV.FORMAT)
                if msg == GV.DISCONNECT_MESSAGE or msg == '':
                    connect = False
            conn.close()
            print(f'[DISCONNECT] Client Close !!!')

        def starting():
            server.listen()
            print(f'Socket Listening .... {ADDR}')
            while True:
                conn, addr = server.accept()
                # thread = threading.Thread(target=handle_client, args=(conn, addr))
                # thread.daemon = True
                # thread.start()
                handle_client(conn, addr)

        def alive_thread(dt):
            time.sleep(10)
            return False

        starting()