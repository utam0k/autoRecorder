import sys


py_3 = int(sys.version_info.major) is 3
if py_3:
    import configparser
else:
    import ConfigParser as configparser

CONF = configparser.ConfigParser()
CONF.read('./config.ini')

if py_3:
    CONF = CONF['CLIENT']
else:  # pragma: no cover
    tmp = CONF.items('CLIENT')
    CONF = {}
    for key, value in tmp:
        CONF[key] = value
