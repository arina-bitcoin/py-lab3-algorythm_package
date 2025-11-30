import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    if seed:
        random.seed(seed)
    
    if distinct:
        if hi - lo + 1 < n:
            raise ValueError("Range too small for distinct values")
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]

def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    if seed:
        random.seed(seed)
    arr = list(range(n))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    if seed:
        random.seed(seed)
    unique_values = list(range(k_unique))
    return [random.choice(unique_values) for _ in range(n)]

def reverse_sorted(n: int) -> list[int]:
    return list(range(n, 0, -1))

def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    if seed:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]

