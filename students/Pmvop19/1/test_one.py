# -*- coding: utf-8 -*-

"""Tests for framework."""

from datetime import datetime


def is_adult(
    input_function=input,
    today_function=datetime.now,
):
    """Is person 18 y.o. or older."""
    users_birthday = datetime.strptime(
        input_function('Your birstday:'),
        '%Y.%m.%d',
    )
    delta = today_function() - users_birthday
    return delta.days / 365 >= 18


def is_null(input_number):
    """Is number equal to 0."""
    return input_number > 0


def test_is_adult():
    """Test for test_is_adult function."""
    assert is_adult(
        lambda _: '1905.04.01',
        lambda: datetime(year=2019, month=9, day=1),
    )
    assert is_adult(
        lambda _: '2018.04.01',
        lambda: datetime(year=2019, month=9, day=1),
    ) is False


def test_is_null():
    """Test for test_is_null function."""
    assert is_null(15)
    assert is_null(0) is False
    assert is_null(-15) is False
