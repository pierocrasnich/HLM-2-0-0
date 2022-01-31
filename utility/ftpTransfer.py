import gvar as GV
from ftplib import FTP


def transferFile():
    conn = FTP(host='192.168.1.101', user='user', passwd='user')
    conn.cwd('/home/user')
    print(conn.pwd())
    file_to_send = open('gvar.py', 'rb')
    conn.storbinary('STOR gvar.py', file_to_send)
    file_to_send.close()
    conn.quit()

transferFile()