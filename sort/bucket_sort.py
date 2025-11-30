try:  # pragma: no cover
    from .quick_sort import quick_sort
except ImportError:  # pragma: no cover
    from quick_sort import quick_sort  # type: ignore

def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    if not a:
        return []

    if buckets is None:
        buckets = len(a) or 1
    if buckets <= 0:
        raise ValueError("Number of buckets must be positive")

    values = a.copy()
    min_value = min(values)
    max_value = max(values)

    if min_value == max_value:
        return values

    span = max_value - min_value
    bucket_list: list[list[float]] = [[] for _ in range(buckets)]
    for value in values:
        normalized_value = (value - min_value) / span
        bucket_index = min(int(normalized_value * buckets), buckets - 1)
        bucket_list[bucket_index].append(value)

    result: list[float] = []
    for bucket in bucket_list:
        if bucket:
            result.extend(quick_sort(bucket))

    return result


if __name__ == "__main__":
    test_data = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    sorted_data = bucket_sort(test_data)
    print(f"Original: {test_data}")
    print(f"Sorted: {sorted_data}")
