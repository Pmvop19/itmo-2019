# -*- coding: utf-8 -*-

"""Framework for running tests."""
import glob
import os
import traceback
from importlib import util

TEST_PREFIX = 'test_'
FILE_TYPE = '.py'


def check_path(path):
    """Check path."""
    if not path:
        path = os.getcwd()
    return os.path.exists(path)


def find_tests(path):
    """Find tests in path directory."""
    if not path:
        path = os.getcwd()
    return glob.glob('{0}/{1}*{2}'.format(path, TEST_PREFIX, FILE_TYPE))


def run_test(filename):
    """Run tests."""
    spec = util.spec_from_file_location(filename[:-3], filename)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    tests = [
        getattr(module, atr)
        for atr in dir(module)  # noqa: WPS421
        if atr.startswith('test_')
    ]
    resultstring = ''
    for test in tests:
        try:  # noqa: WPS229
            test()
            resultstring += '{0} {1} - ok\n'.format(test.__name__, filename)
        except Exception:
            resultstring += '{0} {1} - fail\n'.format(test.__name__, filename)
            resultstring += '{0}\n'.format(traceback.format_exc())
    return resultstring


if __name__ == '__main__':
    path = input('Input your dir:')  # noqa: S322, WPS421
    if check_path(path):
        tests_files = find_tests(path)
        for test in tests_files:
            print(run_test(test))  # noqa: T001
    else:
        print("Dir incorrect or doesn't exist.")  # noqa: T001
