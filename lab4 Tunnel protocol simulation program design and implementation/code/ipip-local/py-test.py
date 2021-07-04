import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
while 1:
    s = input('>>>').encode('utf-8')
    sk.sendto(s, ('39.97.114.89', 22222))
sk.close()

