# Speed test for Python 3.11
I created a simple speed test to compare Python 3.11 to 3.10 (and 3.9 .. 3.5).

#### Dennis Bakhuis - 8th September 2022
#### https://linkedin.com/in/dennisbakhuis/

## Blog post
This is the code which belongs to a blog post you can find here.

## Requirements
- Python environment to run the tester
- Docker to download each Python Env.

## Usage:
```bash
python run_main_test.py
```

## Monte Carlo Pi estimation
For this I us a Pi estimation. Not sure if this is the best workload but it is at least Python heavy.

## Result
```stdout
The new Python 3.11 took 6.4605 seconds per run.

Python 3.5 took 11.3014 seconds per run.(Python 3.11 is 74.9% faster)
Python 3.6 took 11.4332 seconds per run.(Python 3.11 is 77.0% faster)
Python 3.7 took 10.7465 seconds per run.(Python 3.11 is 66.3% faster)
Python 3.8 took 10.6904 seconds per run.(Python 3.11 is 65.5% faster)
Python 3.9 took 10.9537 seconds per run.(Python 3.11 is 69.5% faster)
Python 3.10 took 8.8467 seconds per run.(Python 3.11 is 36.9% faster)
```

## Result for C++
Build instructions in the folder.
```stdout
Pi is approximately 3.14227 and took 0.25728 seconds to calculate.
Pi is approximately 3.14164 and took 0.25558 seconds to calculate.
Pi is approximately 3.1423 and took 0.25740 seconds to calculate.
Pi is approximately 3.14108 and took 0.25737 seconds to calculate.
Pi is approximately 3.14261 and took 0.25664 seconds to calculate.

Each loop took on average 0.25685 seconds to calculate.
```

