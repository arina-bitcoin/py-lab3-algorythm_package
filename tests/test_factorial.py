import pytest

from tests.module_utils import load_module

factorial_module = load_module("factorial_module", "fib+factorial/factorial.py")


@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (5, 120), (7, 5040)])
def test_factorial_iterative(n, expected):
    assert factorial_module.factorial(n) == expected


@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (5, 120), (7, 5040)])
def test_factorial_recursive(n, expected):
    assert factorial_module.factorial_recursive(n) == expected


def test_factorial_negative_input():
    with pytest.raises(ValueError):
        factorial_module.factorial(-1)
    with pytest.raises(ValueError):
        factorial_module.factorial_recursive(-3)

