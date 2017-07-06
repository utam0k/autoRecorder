import unittest
import sys

from nose.tools import eq_, ok_, raises

from client import config
from test import utils


class ConfigTest(unittest.TestCase):

    @utils.py_3_only
    def test_CONF_keys_3(self):
        keys = list(config.CONF.keys())
        eq_(keys, ['dest_addr', 'dest_port', 'mucsic_xml_path'])

    @utils.py_2_only
    def test_CONF_keys_2(self):
        keys = list(config.CONF.keys())
        expect_keys = ['dest_addr', 'dest_port', 'mucsic_xml_path']
        for key in keys:
            ok_(key in expect_keys)

    def test_python_version(self):
        result = config.py_3
        expect = int(sys.version_info.major)
        if expect is 3:
            ok_(result)
        elif expect is 2:
            ok_(not result)

    @raises(KeyError)
    def test_not_key_CONF_3(self):
        config.CONF['aaaa']
