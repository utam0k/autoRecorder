import time

from server import receive_server
from server.config import CONF


def main():
    receive_server.start(CONF['addr'], int(CONF['port']))
    while True:
        time.sleep(10)


if __name__ == '__main__':
    main()
