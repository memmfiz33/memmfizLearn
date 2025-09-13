import pytest

from math_fuc import add, divide, subtract, sqrt_monneng

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 0) == -1
    assert add(-2, 2) == 0

def test_divide():
    assert divide(4, 2) == 2
    assert divide(-8, -2) == 4

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(-1, 0) == -1
    assert subtract(-2, 2) == -4

def test_sqrt_monneng_ok():
    assert sqrt_monneng(0) == 0
    assert sqrt_monneng(9) == 3

def test_sqrt_monneng_negative():
    with pytest.raises(ValueError):
        sqrt_monneng(-1)