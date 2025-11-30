import pytest

from tests.module_utils import load_module

fibonacci_module = load_module("fibonacci_module", "fib+factorial/fibonachi.py")


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5),
        (10, 55),
    ],
)
def test_fibonacci_iterative(n, expected):
    assert fibonacci_module.fibo(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5),
        (10, 55),
    ],
)
def test_fibonacci_recursive(n, expected):
    assert fibonacci_module.fibo_recursive(n) == expected


def test_fibonacci_negative_input():
    with pytest.raises(ValueError):
        fibonacci_module.fibo(-1)
    with pytest.raises(ValueError):
        fibonacci_module.fibo_recursive(-2)

