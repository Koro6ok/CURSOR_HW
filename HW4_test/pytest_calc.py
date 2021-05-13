import pytest
from function_to_test import Calculator


""" Using pytest lib """

def test_add_():
    assert Calculator.add(2, 4) == 6

def test_substract_():
    assert Calculator.subtract(4, 2) == 2

def test_multiply_():
    assert Calculator.multiply(4, 2) == 8

def test_devide_():
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)





