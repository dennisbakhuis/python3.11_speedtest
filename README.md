# Speed test for Python 3.11
I created a simple speed test to compare Python 3.11 to 3.10 (and 3.9 .. 3.5).
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

## Calculated results by continuous integration
You can see [the latest results](https://github.com/dennisbakhuis/python3.11_speedtest/actions/workflows/run.yml) in Github Actions for different languages as
well as different versions of Python. The results are collected in a JSON artifact. Below is an example output:

```json
{
    "Cython": 0.0273,
    "C": 0.0355,
    "Julia": 0.0368,
    "Go": 0.0846,
    "Numba": 0.0958,
    "Rust": 0.1559,
    "Python_3.11": 1.0992,
    "Python_3.9": 1.4127,
    "Python_3.10": 1.4161,
    "Python_3.7": 1.4191,
    "Python_3.8": 1.8726
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

## Results summary
| Language    | Result (seconds) |
|-------------|------------------|
| Cython      | 0.0273           |
| C++         | 0.0355           |
| Julia       | 0.0368           |
| Go          | 0.0846           |
| Numba       | 0.0958           |
| Rust        | 0.1559           |
| Python 3.11 | 1.0992           |
| Python 3.9  | 1.4127           |
| Python 3.10 | 1.4161           |
| Python 3.7  | 1.4191           |
| Python 3.8  | 1.8726          |


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
