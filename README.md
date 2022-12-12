# Speed test for Python 3.11
I created a simple speed test to compare Python 3.11 to 3.10 (and 3.9 .. 3.5).

#### Dennis Bakhuis - 8th September 2022
#### https://linkedin.com/in/dennisbakhuis/

## Additional contributions:
- Rust contribution by [Luander Ribeiro](https://linkedin.com/in/luander/) -> [github](https://github.com/luander).
- Julia contribution by Xiaoguang Pan (潘小光) -> [github](https://github.com/panxiaoguang).
- Golang and automation contribution by [Greg Hellings](https://www.linkedin.com/in/gregory-hellings-97b15058/) -> [github](https://github.com/greg-hellings/)


## Blog post
This is the code which belongs to a blog post you can find [here](https://towardsdatascience.com/python-3-14-will-be-faster-than-c-a97edd01d65d).

## Requirements
- Python environment to run the tester
- Docker to download each Python Env.

## Usage:
```bash
python run_main_test.py
```

## Monte Carlo Pi estimation
For this I us a Pi estimation. Not sure if this is the best workload but it is at least Python heavy.

## Sample Results in CI

You can see [the latest results](actions/workflows/run.yml) in Github Actions for different languages as
well as different versions of Python.

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

## Result for Rust
Build instructions in folder.
```stdout
Pi is approximately 3.141846 and took 0.135379923 seconds to calculate
Pi is approximately 3.1414772 and took 0.141171119 seconds to calculate
Pi is approximately 3.1422468 and took 0.142733311 seconds to calculate
Pi is approximately 3.1424972 and took 0.143618234 seconds to calculate
Pi is approximately 3.1418892 and took 0.144456931 seconds to calculate
Pi is approximately 3.1420588 and took 0.145583613 seconds to calculate
Pi is approximately 3.1423404 and took 0.14586195 seconds to calculate
Pi is approximately 3.141976 and took 0.144568619 seconds to calculate
Pi is approximately 3.140442 and took 0.144518661 seconds to calculate
Pi is approximately 3.1409804 and took 0.144981119 seconds to calculate

Each loop took on average 0.143287348 seconds to calculate.
```

## Result for Julia
Build instructions in folder.
```stdout
Pi is approximately 3.1412084 and took 0.032 seconds to calculate
Pi is approximately 3.141088 and took 0.033 seconds to calculate
Pi is approximately 3.1412732 and took 0.033 seconds to calculate
Pi is approximately 3.1419132 and took 0.033 seconds to calculate
Pi is approximately 3.1411956 and took 0.033 seconds to calculate
Pi is approximately 3.1420764 and took 0.033 seconds to calculate
Pi is approximately 3.1419316 and took 0.033 seconds to calculate
Pi is approximately 3.1424968 and took 0.034 seconds to calculate
Pi is approximately 3.1413764 and took 0.033 seconds to calculate
Pi is approximately 3.1416868 and took 0.034 seconds to calculate
Each loop took on average 0.033100000000000004 seconds to calculate.
```
