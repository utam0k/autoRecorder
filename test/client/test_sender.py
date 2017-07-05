import unittest
import threading
import socketserver

from nose.tools import eq_

from client import sender


HOST, PORT = 'localhost', 5555
recv_data = None

class DummyServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


class DummyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        length = int(self.request.recv(10).strip().decode('utf-8'))
        recv_data = self.request.recv(length).strip().decode('utf-8')


class SenderTest(unittest.TestCase):

    def setUp(self):
        self.server = DummyServer((HOST, PORT), DummyHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.setDaemon(True)
        self.server_thread.start()

    def tearDown(self):
        self.server.shutdown()

    def test_send_string(self):
        data = 'aaaa'
        recv = sender.send(HOST, PORT, data)
        eq_(recv_data, recv)
