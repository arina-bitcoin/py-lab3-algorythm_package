import pytest

from sort import heap_sort, heap_sort_custom
from tests.test_generator import (
    many_duplicates,
    nearly_sorted,
    rand_int_array,
    reverse_sorted,
)


@pytest.mark.parametrize(
    "dataset",
    [
        rand_int_array(25, -100, 100, seed=21),
        nearly_sorted(40, swaps=4, seed=22),
        many_duplicates(30, k_unique=5, seed=23),
        reverse_sorted(10),
        [],
        [42],
    ],
    ids=[
        "random",
        "nearly_sorted",
        "duplicates",
        "reverse",
        "empty",
        "single",
    ],
)
def test_heap_sort(dataset):
    original = dataset.copy()
    assert heap_sort(dataset) == sorted(dataset)
    assert dataset == original  # must not mutate input


def test_heap_sort_preserves_duplicates():
    data = [5, 1, 3, 5, 2, 5, 0]
    assert heap_sort(data) == sorted(data)


def test_heap_sort_custom_with_key_and_cmp():
    data = [
        {"name": "alice", "score": 88},
        {"name": "bob", "score": 95},
        {"name": "carol", "score": 75},
    ]
    sorted_by_score = heap_sort_custom(data, key=lambda item: item["score"])
    assert [item["name"] for item in sorted_by_score] == ["carol", "alice", "bob"]

    def cmp_by_name_desc(left, right):
        return (right["name"] > left["name"]) - (right["name"] < left["name"])

    sorted_by_name_desc = heap_sort_custom(data, cmp=cmp_by_name_desc)
    assert [item["name"] for item in sorted_by_name_desc] == ["carol", "bob", "alice"]

