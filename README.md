# StatsTester
StatsTester is open-source software for Statistic Tests. It includes module for t-test and f-test. StatsTest depends on NumPy and SciPy.

# Install
```
$ python setup.py install
```
or
```
$ pip install statstester
```

# Test
```
$ python setup.py test
```

# How to Use
## Basic usage
This program help to peform the statistical test.
```
import statstester.statstester
import numpy.random
import as np
x0 = numpy.random.rand(20)
x1 = numpy.random.rand(20)
t, p = statstester.statstester.t_test(x0, x1) # t-test
f = statstester.statstester.t_test(x0, x1) # f-test
```

## T-test between 2 lines
```
import statstester.statstester
def funcA(x, a, b):
        return a*x + b

x = np.linspace(0, 10, 100)
e = np.random.normal(size=100)
x0 = x
y0 = funcA(x0, 1, 2) + e
e = np.random.normal(size=100)
x1 = x
y1 = funcA(x, 1, 2) + e
y0_l = funcA(x, 1, 2)
stastester.statstester.two_line_t_test([x, y0], [x, y1], alpha = 0.1) # => Comparing the [x, y0] and [x, y1]
```

# License Information
See the file `LICENSE` for information on the history of this software.