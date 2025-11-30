def radix_sort(a: list[int], base: int = 10) -> list[int]:
    if not a:
        return []
    if base < 2:
        raise ValueError("Base must be at least 2")

    def sort_non_negative(nums: list[int]) -> list[int]:
        if not nums:
            return []
        output = nums.copy()
        max_val = max(output)
        exp = 1
        while max_val // exp > 0:
            buckets = [[] for _ in range(base)]
            for num in output:
                digit = (num // exp) % base
                buckets[digit].append(num)
            output = [value for bucket in buckets for value in bucket]
            exp *= base
        return output

    positives = [value for value in a if value >= 0]
    negatives = [-value for value in a if value < 0]

    sorted_pos = sort_non_negative(positives)
    sorted_neg = sort_non_negative(negatives)
    sorted_neg = [-value for value in reversed(sorted_neg)]

    return sorted_neg + sorted_pos



if __name__ == "__main__":
    print("Testing Radix Sort")
    print("=" * 50)
    
    # Тест 1: Обычный случай
    test1 = [4, 2, 2, 8, 3, 3, 1]
    print(f"Test 1 - Basic: {test1}")
    result1 = radix_sort(test1)
    print(f"Sorted: {result1}")
    print(f"Correct: {result1 == sorted(test1)}")
    print()
    
    # Тест 2: Отрицательные числа
    test2 = [4, -2, 2, -8, 3, 3, 1]
    print(f"Test 2 - With negatives: {test2}")
    result2 = radix_sort(test2)
    print(f"Sorted: {result2}")
    print(f"Correct: {result2 == sorted(test2)}")
    print()
    
    # Тест 3: Один элемент
    test3 = [5]
    print(f"Test 3 - Single element: {test3}")
    result3 = radix_sort(test3)
    print(f"Sorted: {result3}")
    print(f"Correct: {result3 == sorted(test3)}")
    print()
    
    # Тест 4: Пустой список
    test4 = []
    print(f"Test 4 - Empty list: {test4}")
    result4 = radix_sort(test4)
    print(f"Sorted: {result4}")
    print(f"Correct: {result4 == sorted(test4)}")
    print()
    
    # Тест 5: Все одинаковые элементы
    test5 = [7, 7, 7, 7, 7]
    print(f"Test 5 - All same: {test5}")
    result5 = radix_sort(test5)
    print(f"Sorted: {result5}")
    print(f"Correct: {result5 == sorted(test5)}")
    print()
    
    # Тест 6: Большой диапазон
    test6 = [1, 100, 50, 25, 75]
    print(f"Test 6 - Large range: {test6}")
    result6 = radix_sort(test6)
    print(f"Sorted: {result6}")
    print(f"Correct: {result6 == sorted(test6)}")
    print()
    
    # Тест 7: Стабильность (проверка с помощью stable версии)
    test7 = [1, 2, 1, 3, 2]  # Два элемента '1' и два элемента '2'
    print(f"Test 7 - Stability test: {test7}")
    result7 = radix_sort(test7)
    print(f"Stable sorted: {result7}")
    print(f"Correct: {result7 == sorted(test7)}")

