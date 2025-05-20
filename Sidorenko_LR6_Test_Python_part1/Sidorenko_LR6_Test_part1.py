from Sidorenko_LR6_Methods_part1 import average_grade, is_good, t_ver_user_inp
import pytest


def test_average():
    assert average_grade(4.3, 4.1, 3.9) == 4.1
    assert average_grade(2.3, 3.1, 3.9) ==3.1
def test_good_grade():
    assert is_good(4.3, 4.1, 3.9) == True
    assert is_good(2.3, 3.1, 3.9) == False
def test_user_inp():
    assert t_ver_user_inp(-2) == False
    assert t_ver_user_inp("str") == False
    assert t_ver_user_inp(2) == 3