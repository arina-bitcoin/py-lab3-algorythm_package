import argparse
import json
import subprocess
import sys
from typing import Callable, Iterable

from stack.stack import Stack
from sort import (
    bubble_sort,
    bucket_sort,
    counting_sort,
    heap_sort,
    quick_sort,
    radix_sort,
)
from tests.banch_marks import (
    BENCHMARK_ALGOS,
    demo_benchmark,
    format_benchmark_results,
)
from tests.module_utils import load_module

SORT_ALGOS: dict[str, Callable[[list], list]] = {
    "bubble": bubble_sort,
    "bucket": bucket_sort,
    "counting": counting_sort,
    "heap": heap_sort,
    "quick": quick_sort,
    "radix": radix_sort,
}

def parse_values(raw_values: Iterable[str], *, as_float: bool) -> list[int] | list[float]:
    converter = float if as_float else int
    return [converter(value) for value in raw_values]


def handle_sort(args: argparse.Namespace) -> int:
    algo = SORT_ALGOS[args.algo]
    if args.algo in ("radix", "counting") and args.floats:
        print(f"Error: {args.algo} sort does not support floating point numbers.")
        return 1
    values = parse_values(args.values, as_float=args.floats)
    result = algo(values.copy())
    print("Input :", values)
    print("Sorted:", result)
    return 0


def handle_benchmark(args: argparse.Namespace) -> int:
    algo_names = args.algos
    skip_message = None
    if algo_names is None and args.size > 2_000 and "bubble" in BENCHMARK_ALGOS:
        algo_names = [name for name in BENCHMARK_ALGOS if name != "bubble"]
        skip_message = (
            "Bubble sort skipped for large sample sizes. "
            "Use --algos bubble ... to include it explicitly."
        )

    results = demo_benchmark(sample_size=args.size, runs=args.runs, algo_names=algo_names)
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(format_benchmark_results(results))
    if skip_message:
        print(skip_message)
    return 0


def handle_test(args: argparse.Namespace) -> int:
    command = ["pytest", *args.pytest_args]
    completed = subprocess.run(command, check=False)
    return completed.returncode


def handle_menu(args: argparse.Namespace) -> int:  # pragma: no cover - interactive helper
    """Simple text menu to perform multiple actions in one run."""

    while True:
        print(
            "\nMain menu\n"
            "1) Sort numbers\n"
            "2) Run benchmarks\n"
            "3) Run tests\n"
            "4) Factorial\n"
            "5) Fibonacci\n"
            "6) Try Stack\n"
            "0) Exit\n"
        )
        choice = input("Choose option: ").strip()

        if choice == "0":
            return 0

        if choice == "1":
            algo_name = input(f"Algorithm {sorted(SORT_ALGOS.keys())}: ").strip()
            if algo_name not in SORT_ALGOS:
                print("Unknown algorithm.")
                continue
            raw = input("Values (space-separated): ").split()
            as_float = input("Treat as floats? [y/N]: ").strip().lower().startswith("y")
            # Radix and counting sort don't support floats
            if algo_name in ("radix", "counting") and as_float:
                print(f"Error: {algo_name} sort does not support floating point numbers.")
                continue
            values = parse_values(raw, as_float=as_float)
            result = SORT_ALGOS[algo_name](values.copy())
            print("Input :", values)
            print("Sorted:", result)
            continue

        if choice == "2":
            try:
                size = int(input("Sample size (default 5000): ") or "5000")
                runs = int(input("Runs per algorithm (default 3): ") or "3")
            except ValueError:
                print("Invalid numeric input.")
                continue
            algo_input = input(
                f"Algorithms (space-separated from {sorted(BENCHMARK_ALGOS.keys())}, empty = auto): "
            ).split()
            algo_names = algo_input or None
            try:
                results = demo_benchmark(sample_size=size, runs=runs, algo_names=algo_names)
            except ValueError as exc:
                print(f"Error: {exc}")
                continue
            print(format_benchmark_results(results))
            continue

        if choice == "3":
            pattern = input("pytest -k <pattern> (empty = all tests): ").strip()
            cmd = ["pytest"]
            if pattern:
                cmd += ["-k", pattern]
            completed = subprocess.run(cmd, check=False)
            print(f"pytest exited with code {completed.returncode}")
            continue

        if choice in {"4", "5"}:
            try:
                n = int(input("n = ").strip())
            except ValueError:
                print("n must be an integer.")
                continue

            if choice == "4":
                factorial_module = load_module("factorial_module", "fib+factorial/factorial.py")
                print("factorial      :", factorial_module.factorial(n))
                print("factorial_rec  :", factorial_module.factorial_recursive(n))
            else:
                fib_module = load_module("fibonacci_module", "fib+factorial/fibonachi.py")
                print("fibo           :", fib_module.fibo(n))
                print("fibo_recursive :", fib_module.fibo_recursive(n))
            continue

        if choice == "6":
            stack = Stack()
            print("\n Stack Menu:")
            print("Commands: push <value>, pop, peek, min, len, empty, show, quit")
            while True:
                try:
                    cmd = input("Stack> ").strip().split()
                    if not cmd:
                        continue
                    if cmd[0] == "quit":
                        break
                    elif cmd[0] == "push":
                        if len(cmd) < 2:
                            print("Usage: push <value>")
                            continue
                        try:
                            value = int(cmd[1])
                            stack.push(value)
                            print(f"Pushed {value}")
                        except ValueError:
                            print("Value must be an integer")
                    elif cmd[0] == "pop":
                        try:
                            value = stack.pop()
                            print(f"Popped {value}")
                        except IndexError as e:
                            print(f"Error: {e}")
                    elif cmd[0] == "peek":
                        try:
                            value = stack.peek()
                            print(f"Top: {value}")
                        except IndexError as e:
                            print(f"Error: {e}")
                    elif cmd[0] == "min":
                        try:
                            value = stack.min()
                            print(f"Minimum: {value}")
                        except IndexError as e:
                            print(f"Error: {e}")
                    elif cmd[0] == "len":
                        print(f"Length: {len(stack)}")
                    elif cmd[0] == "empty":
                        print(f"Empty: {stack.is_empty()}")
                    elif cmd[0] == "show":
                        if stack.is_empty():
                            print("Stack is empty")
                        else:
                            items = []
                            temp_stack = Stack()
                            while not stack.is_empty():
                                val = stack.pop()
                                items.append(val)
                                temp_stack.push(val)
                            # Restore stack
                            while not temp_stack.is_empty():
                                stack.push(temp_stack.pop())
                            print(f"Stack (top to bottom): {items}")
                    else:
                        print("Unknown command. Use: push, pop, peek, min, len, empty, show, quit")
                except KeyboardInterrupt:
                    print("\nExiting Stack demo...")
                    break
                except Exception as e:
                    print(f"Error: {e}")
            continue

        print("Unknown option, try again.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Utility entry point for the sorting project.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    sort_parser = subparsers.add_parser("sort", help="Sort a list of numbers with the chosen algorithm.")
    sort_parser.add_argument("algo", choices=sorted(SORT_ALGOS.keys()), help="Algorithm to use.")
    sort_parser.add_argument("values", nargs="+", help="Values to sort.")
    sort_parser.add_argument(
        "--floats",
        action="store_true",
        help="Interpret the provided values as floating point numbers.",
    )
    sort_parser.set_defaults(func=handle_sort)

    benchmark_parser = subparsers.add_parser("benchmark", help="Run demo benchmarks and print timings.")
    benchmark_parser.add_argument("--size", type=int, default=5_000, help="Dataset size per scenario.")
    benchmark_parser.add_argument("--runs", type=int, default=3, help="Repetitions per algorithm.")
    benchmark_parser.add_argument(
        "--algos",
        nargs="+",
        choices=sorted(BENCHMARK_ALGOS.keys()),
        help="Space-separated list of algorithms to benchmark (defaults adapt to data size).",
    )
    benchmark_parser.add_argument(
        "--json",
        action="store_true",
        help="Print raw JSON instead of a formatted table.",
    )
    benchmark_parser.set_defaults(func=handle_benchmark)

    subparsers.add_parser("test", help="Run the pytest suite (passes extra args through).").set_defaults(
        func=handle_test
    )

    subparsers.add_parser("menu", help="Interactive menu for multiple successive actions.").set_defaults(
        func=handle_menu
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args, extra = parser.parse_known_args(argv)

    if getattr(args, "command", None) == "test":
        args.pytest_args = extra
        extra = []

    if extra:
        parser.error(f"unrecognized arguments: {' '.join(extra)}")

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

