
import pytest
from project import calculate_derivative
from project import date
from project import inclination_slope

def main():
    test_date()
    test_calculate_derivative()
    test_inclination_slope()


def test_date():
    with pytest.raises(ValueError):
        date("abc")
        date("")
        date(" ")
        date(":")

def test_calculate_derivative():
    assert calculate_derivative([1, 0, 0], 5) == 10
    assert calculate_derivative([2, 5, 5], 5) == 25
    assert calculate_derivative([2, -5, 5], 5) == 15
    assert calculate_derivative([1, 1], 5) == 1
    assert calculate_derivative([0, 1], 5) == 0

def test_inclination_slope():
    assert inclination_slope(4) == 76
    assert inclination_slope(-4) == -76


if __name__ == "__main__":
    main()
