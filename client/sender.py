import socket


def send(host, port, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    length = '{0:010d}'.format(len(data))
    sock.connect((host, port))
    sock.send(bytes(length + data, "utf-8"))
    sock.close()
