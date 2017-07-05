import json

from client.parse import parse
from client import sender


HOST, PORT = 'localhost', 5555


def main():
    data = parse('./test/data/example.xml')
    sender.send(HOST, PORT, json.dumps(data))

if __name__ == '__main__':
    main()
