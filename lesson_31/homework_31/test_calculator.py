import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_subtract(calc):
    assert calc.subtract(5, 2) == 3

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12

def test_divide(calc):
    assert calc.divide(10, 2) == 5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(10, 0)

def test_power(calc):
    assert calc.power(2, 3) == 8

def test_modulo(calc):
    assert calc.modulo(10, 3) == 1

def test_modulo_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot modulo by zero."):
        calc.modulo(10, 0)