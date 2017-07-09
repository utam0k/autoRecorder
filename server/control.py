import pickle

from server.config import CONF


def run():
    """ Control RaspberryPi """
    with open(CONF['pickle_path'], mode='rb') as f:
        data = pickle.load(f)

    print(data)

if __name__ == '__main__':
    run()
