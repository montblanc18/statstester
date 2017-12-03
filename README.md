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
>>> import statstester.statstester as stst
>>> import numpy.random
>>> x0 = numpy.random.rand(20)
>>> x1 = numpy.random.rand(20)
>>> t, p = stst.t_test(x0, x1)
>>> print('t:{}, p:{}'.format(t,p)) # t-test
t:0.09000179448963339, p:0.9287585122220914
>>> f = stst.f_test(x0, x1) # f-test
>>> print('f:{}'.format(f))
f:0.6571863043674027
```

## T-test between 2 lines
```
>>> import statstester.statstester as stst
>>> import numpy as np
>>> def funcA(x, a, b):
...     return a * x + b
... 
>>> x = np.linspace(0, 10, 100)
>>> e0 = np.random.normal(size = 100)
>>> x0 = x
>>> y0 = funcA(x0, 1, 2) + e0
>>> e1 = np.random.normal(size = 100)
>>> x1 = x
>>> y1 = funcA(x1, 1, 2) + e1
>>> stst.two_line_t_test([x0, y0], [x1, y1], alpha = 0.1) # => Comparing the [x0, y0] and [x1, y1]

[ Slope ] | t value:-0.016864376838316413 | < t_inv value:1.6526650592326861 means that it is NOT significant by 0.1.
[ Intercept ] | t value:0.13250911943570165 | < t_inv value:1.6526650592326861 means that it is NOT significant by 0.1.
```

# License Information
See the file `LICENSE` for information on the history of this software.