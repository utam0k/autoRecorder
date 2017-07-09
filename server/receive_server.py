import threading
import pickle
import json

from server import config

if config.py_3:
    import socketserver
else:
    import SocketServer as socketserver


def start(host, port):
    server = ReceiveServer((host, port), Handler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    return server


class ReceiveServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        try:
            length = int(self.request.recv(10).strip().decode('utf-8'))
        except:
            print("Error: Receive messeage is not right format")
            self.request.send(b'0')
        print(length)
        data = json.loads(self.request.recv(length).decode('utf-8'))

        with open(config.CONF['pickle_path'], mode='wb') as f:
            pickle.dump(data, f, protocol=2)
        self.request.send(b'1')
