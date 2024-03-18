import sys
import os

# Add the src directory to the Python path
# flake8: noqa
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import pytest
from src.calculations import Calculations


def test_sum():
    assert Calculations.sum(1, 1) == 2
    assert Calculations.sum(8, 12) == 20
    assert Calculations.sum(9, -1021) == -1012


def test_multiplication():
    assert Calculations.multiplication(1, 1) == 1
    assert Calculations.multiplication(0, 3) == 0
    assert Calculations.multiplication(-5, 3) == -15
    assert Calculations.multiplication(5, 8) == 40


def test_division():
    assert Calculations.division(3, 1) == 3.0
    assert Calculations.division(16, 2) == 8.0
    assert Calculations.division(1, 5) == 0.2
    assert Calculations.division(6, -2) == -3.0

    with pytest.raises(ZeroDivisionError):
        Calculations.division(4, 0)
