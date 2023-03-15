# Speed test for Python 3.12

I created a simple speed test to compare Python 3.12 to 3.11 (and 3.10 .. 3.5).
The tests use a Monte Carlo Pi estimation. This is probably not the best workload for a full Python stress test.

#### Dennis Bakhuis - 8th September 2022

#### https://linkedin.com/in/dennisbakhuis/

## Blog post

This is the code which belongs to a blog post you can find [here](https://towardsdatascience.com/python-3-14-will-be-faster-than-c-a97edd01d65d).

## Additional contributions:

- Rust contribution by [Luander Ribeiro](https://linkedin.com/in/luander/) -> [github](https://github.com/luander).
- Julia contribution by Xiaoguang Pan (潘小光) -> [github](https://github.com/panxiaoguang).
- Golang and automation contribution by [Greg Hellings](https://www.linkedin.com/in/gregory-hellings-97b15058/) -> [github](https://github.com/greg-hellings/)
- Cython and Numba contribution by [Jev Kuznetsov](https://www.linkedin.com/in/jev-kuznetsov/) -> [github](https://github.com/sjev)
- C++ (improved) by [Juraj Szitas](https://www.linkedin.com/in/juraj-szitas/) -> [github](https://github.com/JSzitas)

## Calculated results by continuous integration

You can see [the latest results](https://github.com/dennisbakhuis/python3.11_speedtest/actions/workflows/run.yml) in Github Actions for different languages as
well as different versions of Python. The results are collected in a JSON artifact. Below is an example output:

```json
{
  "Julia": 0.0448,
  "Go": 0.0774,
  "Numba": 0.1626,
  "Rust": 0.1755,
  "Cpp": 0.2071,
  "Cython": 0.2703,
  "C": 0.4208,
  "Python_3.11": 12.1766,
  "Python_3.9": 14.1459,
  "Python_3.10": 14.3943,
  "Python_3.7": 16.0291,
  "Python_3.8": 18.6563
}
```

## Run original test using Docker

### Requirements

- Python environment to run the tester
- Docker to download each Python Env.

### Usage:

```bash
cd pi_estimates/Python
python run_main_test.py
```

## Original results

```stdout
The new Python 3.11 took 6.4605 seconds per run.

Python 3.5 took 11.3014 seconds per run.(Python 3.11 is 74.9% faster)
Python 3.6 took 11.4332 seconds per run.(Python 3.11 is 77.0% faster)
Python 3.7 took 10.7465 seconds per run.(Python 3.11 is 66.3% faster)
Python 3.8 took 10.6904 seconds per run.(Python 3.11 is 65.5% faster)
Python 3.9 took 10.9537 seconds per run.(Python 3.11 is 69.5% faster)
Python 3.10 took 8.8467 seconds per run.(Python 3.11 is 36.9% faster)
```
