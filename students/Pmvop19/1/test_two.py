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
    assert my_sum(5, 2) == 7


def test_mult():
    """Multiply test."""
    assert my_mult(2, 2) == 4
    assert my_mult(1, 1) == 1
    assert my_mult(7, 0) == 0
    assert my_mult(6, 4) == 24
    assert my_mult(-6, 4) == -24
    assert my_mult(6, -4) == -24
    assert my_mult(-6, -4) == 24
    assert my_mult(float('nan'), 1)


def test_div():
    """Division test."""
    assert round(my_div(1, 1)) == 1
    assert isinstance(my_div(1, 1), float)
    assert round(my_div(5, 2)) == 2
    assert round(my_div(6, 2)) == 3

    try:
        my_div(1, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False  # noqa: B011, WPS444
