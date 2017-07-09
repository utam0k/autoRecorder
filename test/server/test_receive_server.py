import unittest
import socket
import json

from nose.tools import eq_

from server import receive_server


HOST, PORT = 'localhost', 5000


class ReceiveServerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = receive_server.start(HOST, PORT)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def tearDown(self):
        self.sock.close()

    def test_receive_suceed(self):
        test_data = [[{'duration': 2, 'pitch': {'octave': 4, 'step': 'G'}}],
                     [{'duration': 3, 'pitch': {'octave': 4, 'step': 'F'}},
                      {'duration': 1, 'pitch': {'octave': 4, 'step': 'E'}},
                      {'duration': 2, 'pitch': {'octave': 4, 'step': 'E'}},
                      {'duration': 1, 'pitch': {'octave': 4, 'step': 'B'}},
                      {'duration': 1, 'pitch': {'octave': 4, 'step': 'G'}}]]
        length = '{0:010d}'.format(len(str(test_data)))
        send_data = (length + json.dumps(test_data)).encode('utf-8')
        self.sock.connect((HOST, PORT))
        self.sock.send(send_data)
        receive = self.sock.recv(1)
        eq_(receive, b'1')

    def test_receive_filed(self):
        test_data = [[{'duration': 2, 'pitch': {'octave': 4, 'step': 'G'}}],
                     [{'duration': 3, 'pitch': {'octave': 4, 'step': 'F'}},
                      {'duration': 1, 'pitch': {'octave': 4, 'step': 'E'}},
                      {'duration': 2, 'pitch': {'octave': 4, 'step': 'E'}},
                      {'duration': 1, 'pitch': {'octave': 4, 'step': 'B'}},
                      {'duration': 1, 'pitch': {'octave': 4, 'step': 'G'}}]]
        length = 'aa'
        send_data = (length + json.dumps(test_data)).encode('utf-8')
        self.sock.connect((HOST, PORT))
        self.sock.send(send_data)
        receive = self.sock.recv(1)
        eq_(receive, b'0')
