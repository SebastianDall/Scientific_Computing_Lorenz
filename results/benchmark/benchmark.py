import timeit
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from lorenz.lorenz import Lorenz
from lorenz.plot_lorenz import plot_lorenz2D, plot_lorenz3D


def benchmark_functions(functions: list) -> list:
    """Benchmark a list of functions

    This function will iterate through a list of tuples containing the name of the function and the function itself. It will then measure the time it takes to execute each function.

    Args:
        functions:
            A list of tuples with the first element being the name of the function and the second element being the function itself.

    Returns:
        A list of tuples with the first element being the name of the function and the second element being the time it took to execute the function.

    Examples:
        benchmark_functions([("foo", lambda: print("foo"))])

    """
    times = []
    for name, func in functions:
        start_time = timeit.default_timer()
        func()
        elapsed = timeit.default_timer() - start_time
        times.append((name, elapsed))
    return times


def main():
    # Define your functions and arguments
    functions = [
        ("step_euler", lambda: Lorenz((0.01, 0.01, 0.01)).step_euler()),
        ("solve_euler", lambda: Lorenz((0.01, 0.01, 0.01)).solve()),
        (
            "plot_euler2D",
            lambda: plot_lorenz2D(
                Lorenz((0.01, 0.01, 0.01)),
                filename="results/benchmark/plot_euler2D.png",
            ),
        ),
        (
            "plot_euler3D",
            lambda: plot_lorenz3D(
                Lorenz((0.01, 0.01, 0.01)),
                filename="results/benchmark/plot_euler3D.png",
            ),
        ),
    ]

    # Measure execution time for each function
    times = benchmark_functions(functions)
    print(times)


if __name__ == "__main__":
    main()
