from typing import Any, Callable, TypeVar
from random import choice

from ._keycmp import decorate_with_key_cmp, undecorate

T = TypeVar("T")


def quick_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a
    center = a[choice(range(len(a)))]
    left = [x for x in a if x < center]
    middle = [x for x in a if x == center]
    right = [x for x in a if x > center]
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_custom(
    a: list[T],
    *,
    key: Callable[[T], Any] | None = None,
    cmp: Callable[[T, T], int] | None = None,
) -> list[T]:
    """Quick sort variant that accepts optional key/cmp callbacks."""

    decorated = decorate_with_key_cmp(a, key=key, cmp=cmp)
    sorted_decorated = quick_sort(decorated)
    return undecorate(sorted_decorated)


if __name__ == "__main__":
    print("Testing Quick Sort")
    print("=" * 50)
    
    # Тест 1: Обычный случай
    test1 = [4, 2, 2, 8, 3, 3, 1]
    print(f"Test 1 - Basic: {test1}")
    result1 = quick_sort(test1)
    print(f"Sorted: {result1}")
    print(f"Correct: {result1 == sorted(test1)}")
    print()
    
    # Тест 2: Отрицательные числа
    test2 = [4, -2, 2, -8, 3, 3, 1]
    print(f"Test 2 - With negatives: {test2}")
    result2 = quick_sort(test2)
    print(f"Sorted: {result2}")
    print(f"Correct: {result2 == sorted(test2)}")
    print()
    
    # Тест 3: Один элемент
    test3 = [5]
    print(f"Test 3 - Single element: {test3}")
    result3 = quick_sort(test3)
    print(f"Sorted: {result3}")
    print(f"Correct: {result3 == sorted(test3)}")
    print()
    
    # Тест 4: Пустой список
    test4 = []
    print(f"Test 4 - Empty list: {test4}")
    result4 = quick_sort(test4)
    print(f"Sorted: {result4}")
    print(f"Correct: {result4 == sorted(test4)}")
    print()
    
    # Тест 5: Все одинаковые элементы
    test5 = [7, 7, 7, 7, 7]
    print(f"Test 5 - All same: {test5}")
    result5 = quick_sort(test5)
    print(f"Sorted: {result5}")
    print(f"Correct: {result5 == sorted(test5)}")
    print()
    
    # Тест 6: Большой диапазон
    test6 = [1, 100, 50, 25, 75]
    print(f"Test 6 - Large range: {test6}")
    result6 = quick_sort(test6)
    print(f"Sorted: {result6}")
    print(f"Correct: {result6 == sorted(test6)}")
    print()
    
    # Тест 7: Стабильность (проверка с помощью stable версии)
    test7 = [1, 2, 1, 3, 2]  # Два элемента '1' и два элемента '2'
    print(f"Test 7 - Stability test: {test7}")
    result7 = quick_sort(test7)
    print(f"Stable sorted: {result7}")
    print(f"Correct: {result7 == sorted(test7)}")

