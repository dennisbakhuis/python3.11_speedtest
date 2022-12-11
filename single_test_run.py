#!/usr/bin/env python

#################################
# Simple Python 3.11 speed test #
#################################
# Author: Dennis Bakhuis        #
# Date: 2022-09-02              #
# License: MIT                  #
#################################
import random
import time
import argparse

from numba import njit

def estimate_pi(
    n_points: int,
    show_estimate: bool,
) -> None:
    """
    Simple Monte Carlo Pi estimation calculation.

    Parameters
    ----------
    n_points
        number of random numbers used to for estimation.
    show_estimate
        if True, will show the estimation of Pi, otherwise
        will not output anything.
    """
    within_circle = 0

    for _ in range(n_points):
        x, y = (random.uniform(-1, 1) for v in range(2))
        radius_squared = x**2 + y**2

        if radius_squared <= 1:
            within_circle += 1

    pi_estimate = 4 * within_circle / n_points

    if not show_estimate:
        print("Final Estimation of Pi=", pi_estimate)

@njit
def estimate_pi_numba(
    n_points: int,
    show_estimate: bool,
) -> None:
    """
    Simple Monte Carlo Pi estimation calculation.

    Parameters
    ----------
    n_points
        number of random numbers used to for estimation.
    show_estimate
        if True, will show the estimation of Pi, otherwise
        will not output anything.
    """
    within_circle = 0

    for _ in range(n_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        radius_squared = x**2 + y**2

        if radius_squared <= 1:
            within_circle += 1

    pi_estimate = 4 * within_circle / n_points

    if not show_estimate:
        print("Final Estimation of Pi=", pi_estimate)



def run_test(
    n_points: int,
    n_repeats: int,
    only_time: bool,
    jit: str
) -> None:
    """
    Perform the tests and measure required time.

    Parameters
    ----------
    n_points
        number of random numbers used to for estimation.
    n_repeats
        number of times the test is repeated.
    only_time
        if True will only print the time, otherwise
        will also show the Pi estimate and a neat formatted
        time.
    jit
        type of jit to use none,numba
    """
    fcns = {"none":estimate_pi, "numba": estimate_pi_numba}

    start_time = time.time()



    for _ in range(n_repeats):
        fcns[jit](n_points, only_time)

    if only_time:
        print(f"{(time.time() - start_time)/n_repeats:.4f}")
    else:
        print(f"Test run was done with {n_points=:.2e}")
        print(
            f"Estimating pi took {(time.time() - start_time)/n_repeats:.4f} seconds per run."
        )


def positive_integer(value: str) -> int:
    """Check for positive integer in arg_parse."""
    int_value = int(value)

    if int_value <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")

    return int_value


def main(arguments=None):
    """Main loop in arg parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--n_points",
        help="Number of random points to use for estimating Pi.",
        type=positive_integer,
        default=1_000_000,
    )

    parser.add_argument(
        "--jit",
        help="use compiler options=[none, numba]",
        default="none",
        type=str
    )

    parser.add_argument(
        "-r",
        "--n_repeats",
        help="Number of times to repeat the calculation.",
        type=positive_integer,
        default=5,
    )
    parser.add_argument(
        "--only-time",
        action="store_true",
        default=False,
    )
    args = parser.parse_args()


    run_test(
        args.n_points,
        args.n_repeats,
        args.only_time,
        args.jit
    )


if __name__ == "__main__":
    main()
