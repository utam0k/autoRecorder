import socket

import serial


def send(host, port, data, sock=None, proto='tcp'):
    if type(data) is not bytes:
        try:
            data = str(data).encode('utf-8')
        except ValueError:
            raise ValueError('encoding error')

    length = '{0:010d}'.format(len(data))
    tmp = length.encode('utf-8') + data
    print(tmp)

    if proto == 'tcp':
        sock = sock or socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, int(port)))
        send_f = sock.send
    elif proto == 'serial':
        sock = sock or serial.Serial(port=port)
        send_f = sock.write
    else:
        raise TypeError('sock type is %s' % (type(sock)))

    send_f(tmp)
    sock.close()
