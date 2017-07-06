import json

from client.parse import parse
from client import sender
from client.config import CONF


def main():
    data = parse(CONF['mucsic_xml_path'])
    sender.send(CONF['dest_addr'], int(CONF['dest_port']), json.dumps(data))

if __name__ == '__main__':
    main()
