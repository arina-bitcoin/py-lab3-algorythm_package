import pytest

from sort import counting_sort
from tests.test_generator import many_duplicates, rand_int_array


@pytest.mark.parametrize(
    "dataset",
    [
        [4, 2, 2, 8, 3, 3, 1],
        [4, -2, 2, -8, 3, 3, 1],
        [5],
        [],
        [7, 7, 7, 7, 7],
        [1, 100, 50, 25, 75],
        rand_int_array(50, -20, 20, seed=11),
        many_duplicates(40, k_unique=3, seed=12),
    ],
    ids=[
        "basic",
        "with_negatives",
        "single",
        "empty",
        "all_equal",
        "wide_range",
        "random_window",
        "many_duplicates",
    ],
)
def test_counting_sort_cases(dataset):
    result = counting_sort(dataset.copy())
    assert result == sorted(dataset)

