# -*- coding: utf-8 -*-

"""Tests for framework."""


def my_sum(first, second):
    """Sum function."""
    return first + second


def my_mult(first, second):
    """Multiply function."""
    return first * second


def my_div(first, second):
    """Division function."""
    return first / second


def test_sum():
    """Sum test."""
    assert my_sum(1, 2) == 3
    assert round(my_sum(2.1, 4.2), 2) == 6.3


def test_mult():
    """Multiply test."""
    assert my_mult(2, 2) == 4
    assert my_mult(1, 1) == 1
    assert my_mult(197, 0) == 0
    assert my_mult(6, 4) == 24
    assert my_mult(-6, 4) == -24
    assert my_mult(6, -4) == -24
    assert my_mult(-6, -4) == 24
    assert my_mult(float('nan'), 1)


def test_div():
    """Division test."""
    assert my_div(1, 1) == 1.0
    assert isinstance(my_div(1, 1), float)
    assert my_div(5, 2) == 2.5
    assert my_div(6, 2) == 3.0

    try:
        my_div(1, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False  # noqa: B011, WPS444
