import socket


def send(host, port, data, sock=None):
    if type(data) is not bytes:
        try:
            data = str(data).encode('utf-8')
        except ValueError:
            raise ValueError('encoding error')
    sock = sock or socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    length = '{0:010d}'.format(len(data))
    sock.connect((host, port))
    tmp = length.encode('utf-8') + data
    sock.send(tmp)
    sock.close()
