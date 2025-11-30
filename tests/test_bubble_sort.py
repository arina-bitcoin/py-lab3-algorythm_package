import pytest

from sort import bubble_sort, bubble_sort_custom
from tests.test_generator import (
    many_duplicates,
    nearly_sorted,
    rand_int_array,
    reverse_sorted,
)


@pytest.mark.parametrize(
    "dataset",
    [
        rand_int_array(20, -50, 50, seed=101),
        nearly_sorted(30, swaps=5, seed=11),
        many_duplicates(25, k_unique=4, seed=7),
        reverse_sorted(15),
        [-10, -5, -1, 0, 1, 7, -3, 7],
    ],
    ids=[
        "random_with_negatives",
        "nearly_sorted",
        "duplicates",
        "reverse_sorted",
        "mixed_signs",
    ],
)
def test_bubble_sort(dataset):
    original = dataset.copy()
    result = bubble_sort(dataset.copy())
    assert result == sorted(dataset)
    assert dataset == original  # ensure original data untouched


def test_bubble_sort_custom_key_and_cmp():
    data = ["bbb", "a", "cc"]
    # Sort by length using key
    assert bubble_sort_custom(data, key=len) == ["a", "cc", "bbb"]

    # Sort descending using cmp
    def reverse_cmp(left: str, right: str) -> int:
        return (right > left) - (right < left)

    assert bubble_sort_custom(data, cmp=reverse_cmp) == ["cc", "bbb", "a"]
