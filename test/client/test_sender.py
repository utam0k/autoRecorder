import unittest
from mock import Mock

from nose.tools import eq_

from client import sender


HOST, PORT = 'localhost', 5555


class SenderTest(unittest.TestCase):

    def setUp(self):
        self.sock = Mock()
        self.sock.connect.return_value = None
        self.sock.send.return_value = None
        self.sock.close.return_value = None

    def tearDown(self):
        eq_(self.sock.send.call_count, 1)
        eq_(self.sock.connect.call_count, 1)
        eq_(self.sock.close.call_count, 1)

    def test_send_bytes(self):
        data = 'aaaa'.encode('utf-8')
        length = '{0:010d}'.format(len(data))
        sender.send(HOST, PORT, data, self.sock)

        send_data = self.sock.send.call_args[0][0]
        tmp = length.encode('utf-8') + data
        eq_(send_data, tmp)

    def test_send_str(self):
        data = 'aaaa'
        length = '{0:010d}'.format(len(data))
        sender.send(HOST, PORT, data, self.sock)

        send_data = self.sock.send.call_args[0][0]
        tmp = length + data
        eq_(send_data, tmp.encode('utf-8'))

    def test_send_list(self):
        data = [1, 2, 3, 4]
        length = '{0:010d}'.format(len(str(data)))
        sender.send(HOST, PORT, data, self.sock)

        send_data = self.sock.send.call_args[0][0]
        tmp = length + str(data)
        eq_(send_data, tmp.encode('utf-8'))
