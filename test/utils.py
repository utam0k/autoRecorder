import sys
import functools


py_3 = int(sys.version_info.major) is 3


def py_2_only(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not py_3:
            return func(self, *args, **kwargs)
    return wrapper


def py_3_only(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if py_3:
            return func(self, *args, **kwargs)
    return wrapper
