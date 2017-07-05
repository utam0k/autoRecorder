import socketserver, unittest, threading

from client import main


class DummyServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


class MyRequestHandlerTest(unittest.TestCase):
    def setUp(self):
        self.server = TestServer((HOST, PORT), MyRequestHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.client = socket.create_connection((HOST, PORT))
        self.server_thread.start()

    def tearDown(self):
        self.client.close()
        self.server.shutdown()
