import pytest

from sort import bucket_sort
from tests.test_generator import rand_float_array


@pytest.mark.parametrize(
    "dataset",
    [
        rand_float_array(30, lo=-10.0, hi=10.0, seed=41),
        [5.5, 5.5, 5.5, 5.5],
        [3.2, -1.4, 7.9, 0.0, 3.2],
    ],
    ids=["random_floats", "constant", "mixed_range"],
)
def test_bucket_sort(dataset):
    assert bucket_sort(dataset.copy()) == sorted(dataset)


def test_bucket_sort_rejects_invalid_bucket_count():
    with pytest.raises(ValueError):
        bucket_sort([0.1, 0.2], buckets=0)

