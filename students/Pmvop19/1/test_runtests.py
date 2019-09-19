# -*- coding: utf-8 -*-

"""Tests for framework functions."""
import runtests


def test_find_tests():
    """Test for find_test function."""
    assert runtests.find_tests('.')
    assert runtests.find_tests('')
    assert runtests.find_tests('path') == []  # noqa: WPS520


def test_run_test():
    """Test for run_test function."""
    try:
        runtests.run_test('./test_three.py')
    except Exception:
        assert True
    else:
        assert False  # noqa: B011, WPS444
    assert runtests.run_test('./test_one.py')


def test_check_path():
    """Test for check_path function."""
    assert runtests.check_path('.')
    assert runtests.check_path('')
    assert runtests.check_path('path') is False
