from functools import cmp_to_key
from typing import Any, Callable, Iterable, Sequence, TypeVar

T = TypeVar("T")
DecoratedValue = tuple[Any, int, T]


def decorate_with_key_cmp(
    items: Sequence[T],
    key: Callable[[T], Any] | None = None,
    cmp: Callable[[T, T], int] | None = None,
) -> list[DecoratedValue]:
    """Return tuples suitable for comparison driven sorts.

    Each tuple stores (comparable_key, original_index, original_value) so that
    algorithms can rely on the tuple ordering while we still keep track of the
    payload in the final position.
    """

    if cmp is not None:
        adapter = cmp_to_key(cmp)
        return [(adapter(value), index, value) for index, value in enumerate(items)]

    if key is not None:
        return [(key(value), index, value) for index, value in enumerate(items)]

    return [(value, index, value) for index, value in enumerate(items)]


def undecorate(decorated: Iterable[DecoratedValue]) -> list[T]:
    """Extract the payload from decorated tuples."""

    return [value for _, _, value in decorated]

