from __future__ import annotations

from typing import Any, Callable, TypeVar

from ._keycmp import decorate_with_key_cmp, undecorate

T = TypeVar("T")


def bubble_sort(a: list[int]) -> list[int]:
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def bubble_sort_custom(
    a: list[T],
    *,
    key: Callable[[T], Any] | None = None,
    cmp: Callable[[T, T], int] | None = None,
) -> list[T]:
    """Возвращает отсортированную копию `a`, учитывая опциональные семантики key/cmp."""

    decorated = decorate_with_key_cmp(a, key=key, cmp=cmp)
    n = len(decorated)
    for i in range(n):
        for j in range(0, n - i - 1):
            if decorated[j] > decorated[j + 1]:
                decorated[j], decorated[j + 1] = decorated[j + 1], decorated[j]
    return undecorate(decorated)