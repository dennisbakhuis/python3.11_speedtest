#################################
# Simple Python 3.11 speed test #
#################################
# Author: Dennis Bakhuis        #
# Date: 2022-09-02              #
# License: MIT                  #
#################################
import subprocess
import os

NEW_IMAGE = {'name': 'Python 3.11', 'image': 'python:3.11-rc-slim'}

TEST_IMAGES = [
        {'name': 'Python 3.5', 'image': 'python:3.7-slim'},
        {'name': 'Python 3.6', 'image': 'python:3.7-slim'},
        {'name': 'Python 3.7', 'image': 'python:3.7-slim'},
        {'name': 'Python 3.8', 'image': 'python:3.8-slim'},
        {'name': 'Python 3.9', 'image': 'python:3.9-slim'},
        {'name': 'Python 3.10', 'image': 'python:3.10-slim'},
]

N_POINTS = 10_000_000  # points used to estimate Pi.
N_REPEATS = 10  # times to repeat the test loop.
# N_POINTS = 1_000_000  # points used to estimate Pi.
# N_REPEATS = 2  # times to repeat the test loop.

SCRIPT = "single_test_run.py"


########
# Main #
########
cwd = os.getcwd()


def test_version(image: str) -> float:
    """
    Run single_test on Python Docker image.

    Parameter
    ---------
    image
        full name of the the docker hub Python image.

    Returns
    -------
    run_time
        runtime in seconds per test loop.
    """
    output = subprocess.run([
            'docker',
            'run',
            '-it',
            '--rm',
            '-v',
            f'{cwd}/{SCRIPT}:/{SCRIPT}',
            image,
            'python',
            f'/{SCRIPT}',
            '--n_points',
            str(N_POINTS),
            '--n_repeats',
            str(N_REPEATS),
            '--only-time',
        ],
        capture_output=True,
        text=True,
    )

    avg_time = float(output.stdout.strip())

    return avg_time


# Get test time for current Python version
base_time = test_version(NEW_IMAGE['image'])
print(f"The new {NEW_IMAGE['name']} took {base_time} seconds per run.\n")

# Compare to previous Python versions
for item in TEST_IMAGES:
    ttime = test_version(item['image'])
    print(
        f"{item['name']} took {ttime} seconds per run."
        f"({NEW_IMAGE['name']} is {(ttime / base_time) - 1:.1%} faster)"
    )



