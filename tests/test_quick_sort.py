import pytest

from sort import quick_sort, quick_sort_custom
from tests.test_generator import (
    many_duplicates,
    nearly_sorted,
    rand_int_array,
    reverse_sorted,
)


@pytest.mark.parametrize(
    "dataset",
    [
        rand_int_array(30, -40, 40, seed=31),
        nearly_sorted(35, swaps=6, seed=32),
        many_duplicates(40, k_unique=3, seed=33),
        reverse_sorted(12),
    ],
    ids=["random", "nearly_sorted", "duplicates", "reverse"],
)
def test_quick_sort(dataset):
    original = dataset.copy()
    result = quick_sort(dataset)
    assert result == sorted(dataset)
    assert dataset == original  # quick sort should not mutate source list


def test_quick_sort_handles_empty_and_single():
    assert quick_sort([]) == []
    assert quick_sort([5]) == [5]


def test_quick_sort_custom_key_and_cmp():
    data = [
        {"name": "alice", "age": 30},
        {"name": "bob", "age": 25},
        {"name": "carol", "age": 35},
    ]
    assert quick_sort_custom(data, key=lambda person: person["age"]) == [
        {"name": "bob", "age": 25},
        {"name": "alice", "age": 30},
        {"name": "carol", "age": 35},
    ]

    def reverse_age(left, right):
        return right["age"] - left["age"]

    assert quick_sort_custom(data, cmp=reverse_age)[0]["age"] == 35

