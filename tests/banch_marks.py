from __future__ import annotations

import random
import time
from typing import Callable, Iterable

from sort import bubble_sort, heap_sort, quick_sort

BENCHMARK_ALGOS = {
    "bubble": bubble_sort,
    "heap": heap_sort,
    "quick": quick_sort,
}


def timeit_once(func: Callable, *args, **kwargs) -> float:
    """Return the execution time for a single function invocation."""
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start


def benchmark_sorts(
    arrays: dict[str, list],
    algos: dict[str, Callable[[list], list]],
    *,
    runs: int = 3,
) -> dict[str, dict[str, float]]:
    """Benchmark algorithms against different datasets.

    Each algorithm is executed `runs` times per dataset on a fresh copy of the
    input to avoid cross-test contamination.  The averaged timings (seconds) are
    returned as a nested dictionary.
    """

    if runs <= 0:
        raise ValueError("runs must be positive")

    results: dict[str, dict[str, float]] = {}
    for array_name, array in arrays.items():
        array_results: dict[str, float] = {}
        for algo_name, algo_func in algos.items():
            times = []
            for _ in range(runs):
                arr_copy = array.copy()
                times.append(timeit_once(algo_func, arr_copy))
            array_results[algo_name] = sum(times) / len(times)
        results[array_name] = array_results

    return results


def demo_benchmark(
    sample_size: int = 5_000,
    runs: int = 3,
    algo_names: Iterable[str] | None = None,
) -> dict[str, dict[str, float]]:
    """Convenience helper to benchmark selected algorithms on random data."""

    arrays = {
        "random": [random.randint(-1_000, 1_000) for _ in range(sample_size)],
        "nearly_sorted": sorted(random.sample(range(sample_size * 2), sample_size)),
        "reversed": list(range(sample_size, 0, -1)),
    }

    if algo_names is None:
        selected = list(BENCHMARK_ALGOS.keys())
    else:
        selected = list(algo_names)
        if not selected:
            raise ValueError("algo_names must include at least one algorithm")
        missing = set(selected) - BENCHMARK_ALGOS.keys()
        if missing:
            raise ValueError(f"Unknown algorithms requested: {', '.join(sorted(missing))}")

    algos = {name: BENCHMARK_ALGOS[name] for name in selected}
    return benchmark_sorts(arrays, algos, runs=runs)


def format_benchmark_results(results: dict[str, dict[str, float]]) -> str:
    lines = []
    for array_name, timings in results.items():
        lines.append(f"[{array_name}]")
        for algo, duration in sorted(timings.items(), key=lambda item: item[1]):
            lines.append(f"  {algo:15s}: {duration:.6f} s")
    return "\n".join(lines)


if __name__ == "__main__":
    printed = format_benchmark_results(demo_benchmark())
    print("Benchmark results (seconds):")
    print(printed)