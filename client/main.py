from pprint import pprint as print

from client.parse import parse


def main():
    print(parse('./test/data/example.xml'))

if __name__ == '__main__':
    main()
