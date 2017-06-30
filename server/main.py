from socketserver import BaseRequestHandler

from server import control


class TCPHandler(BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        control.run(self.data)
