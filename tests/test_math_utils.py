from math_utils import mul, mean

def test_mul_basic(small_list):
    assert mul(small_list[0], small_list[1]) == 8

def test_mean_small(small_list):
    assert mean(small_list) == 4

def test_mean_mixed(mixed_list):
    assert mean(mixed_list) == 20

