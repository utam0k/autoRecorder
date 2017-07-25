import json

from client.parse import parse
from client import sender
from client.config import CONF


def main():
    data = parse(CONF['mucsic_xml_path'])
    proto = CONF['proto']
    addr, port = CONF['dest_addr'], CONF['dest_port']
    sender.send(addr, port, json.dumps(data), proto=proto)

if __name__ == '__main__':
    main()
