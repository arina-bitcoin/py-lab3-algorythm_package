import pytest

from sort import radix_sort
from tests.test_generator import rand_int_array, reverse_sorted


@pytest.mark.parametrize(
    "dataset",
    [
        rand_int_array(50, -500, 500, seed=51),
        reverse_sorted(25),
        [0, 0, 0, 0],
        [],
    ],
    ids=["mixed_signs", "reverse", "all_zero", "empty"],
)
def test_radix_sort(dataset):
    assert radix_sort(dataset.copy()) == sorted(dataset)


def test_radix_sort_base_constraints():
    data = [-170, 45, 75, -90, 802, 24, 2, 66, -1]
    assert radix_sort(data, base=8) == sorted(data)
    with pytest.raises(ValueError):
        radix_sort(data, base=1)

