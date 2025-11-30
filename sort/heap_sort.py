from typing import Any, Callable, TypeVar

from ._keycmp import decorate_with_key_cmp, undecorate

T = TypeVar("T")


def _sift_down(arr: list, start: int, end: int) -> None:
    """Move the value at index `start` down the heap until heap property holds."""
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] >= arr[child]:
            break
        arr[root], arr[child] = arr[child], arr[root]
        root = child


def _heapify(arr: list) -> None:
    """Convert the array into a max-heap in-place."""
    for start in range(len(arr) // 2 - 1, -1, -1):
        _sift_down(arr, start, len(arr) - 1)


def heap_sort(a: list[int]) -> list[int]:
    """Return a sorted copy of the provided list using heap sort."""
    if len(a) <= 1:
        return a.copy()

    arr = a.copy()
    _heapify(arr)
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down(arr, 0, end - 1)
    return arr


def heap_sort_custom(
    a: list[T],
    *,
    key: Callable[[T], Any] | None = None,
    cmp: Callable[[T, T], int] | None = None,
) -> list[T]:
    """Heap sort variant that accepts key/cmp callbacks."""

    if len(a) <= 1:
        return a.copy()

    decorated = decorate_with_key_cmp(a, key=key, cmp=cmp)
    arr = decorated.copy()
    _heapify(arr)
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down(arr, 0, end - 1)
    return undecorate(arr)


def main():
    array = [int(item) for item in input().split()]
    print(heap_sort(array))


if __name__ == '__main__':
    main()
