import unittest
import threading
import time
import json

from nose.tools import eq_

from client.config import CONF
from client.main import main

if CONF['py_3']:
    import socketserver
else:
    import SocketServer as socketserver


HOST, PORT = 'localhost', 5555


class DummyServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    recv_data = None


class DummyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        length = int(self.request.recv(10).strip().decode('utf-8'))
        data = self.request.recv(length)
        self.server.recv_data = data.strip().decode('utf-8')


class MainTest(unittest.TestCase):

    def setUp(self):
        self.server = DummyServer((HOST, PORT), DummyHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.setDaemon(True)
        self.server_thread.start()

    def tearDown(self):
        self.server.shutdown()

    def __wait(self, cond, timeout=60):
        s = time.time()
        while cond():
            if time.time() - s > timeout:
                raise Exception('Time out')

    def test_main(self):
        main()
        expect = [[{'duration': 2, 'pitch': {'octave': 4, 'step': 'G'}}],
                  [{'duration': 3, 'pitch': {'octave': 4, 'step': 'F'}},
                   {'duration': 1, 'pitch': {'octave': 4, 'step': 'E'}},
                   {'duration': 2, 'pitch': {'octave': 4, 'step': 'E'}},
                   {'duration': 1, 'pitch': {'octave': 4, 'step': 'B'}},
                   {'duration': 1, 'pitch': {'octave': 4, 'step': 'G'}}]]
        self.__wait(lambda: not self.server.recv_data)
        eq_(json.loads(self.server.recv_data), expect)
