from time import sleep

import pytest

from tests.banch_marks import BENCHMARK_ALGOS, benchmark_sorts, demo_benchmark, timeit_once


def test_timeit_once_measures_elapsed_time():
    def slow_func():
        sleep(0.01)

    duration = timeit_once(slow_func)
    assert duration >= 0.009  # allow for scheduling jitter


def test_benchmark_sorts_returns_results_and_preserves_inputs():
    arrays = {"sample": [3, 2, 1]}

    def algo_sorted(values):
        return sorted(values)

    def algo_reverse(values):
        values.reverse()
        return values

    results = benchmark_sorts(arrays, {"sorted": algo_sorted, "reverse": algo_reverse}, runs=2)
    assert arrays["sample"] == [3, 2, 1]
    assert set(results["sample"].keys()) == {"sorted", "reverse"}
    assert all(duration >= 0 for duration in results["sample"].values())


def test_benchmark_sorts_validates_run_count():
    with pytest.raises(ValueError):
        benchmark_sorts({"a": [1, 2]}, {"sorted": sorted}, runs=0)


def test_demo_benchmark_accepts_algorithm_subset():
    results = demo_benchmark(sample_size=50, runs=1, algo_names=["heap"])
    assert set(results.keys()) == {"random", "nearly_sorted", "reversed"}
    assert set(results["random"]) == {"heap"}

    with pytest.raises(ValueError):
        demo_benchmark(sample_size=10, runs=1, algo_names=[])

    with pytest.raises(ValueError):
        demo_benchmark(sample_size=10, runs=1, algo_names=["unknown"])

