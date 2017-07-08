import sys


py_3 = int(sys.version_info.major) is 3
if py_3:
    import configparser
else:
    import ConfigParser as configparser

CONF = configparser.ConfigParser()
CONF.read('./config.ini')

if py_3:
    CONF = CONF['SERVER']
else:
    tmp = CONF.items('SERVER')
    CONF = {}
    for key, value in tmp:
        CONF[key] = value
