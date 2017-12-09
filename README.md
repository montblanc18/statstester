# StatsTester
StatsTester is open-source software for Statistic Tests. It includes module for t-test and f-test. StatsTest depends on NumPy, SciPy, and Matplotlib.

# Install
```
$ python setup.py install
```
or
```
$ pip install statstester
```

# Test
```bash
$ python setup.py test
```

# How to Use
## Basic usage
This program help to peform the statistical test.
```python
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
```python
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
>>> stst.two_line_t_test([x0, y0], [x1, y1], alpha = 0.1) # two line t_test
[ Slope ] | t value:1.9747106131647987 | > t_inv value:1.2858857707030413 means that it is significant by 0.1.
[ Intercept ] | t value:-1.7192242957174544 | > t_inv value:1.2858857707030413 means that it is significant by 0.1.
>>> stst.quick_look_two_data([x0, y0], [x1, y1], saveflag = True, savename = 'temp.png') # quick look
[ Slope ] | t value:1.9747106131647987 | > t_inv value:1.6526650592326861 means that it is significant by 0.05.
[ Intercept ] | t value:-1.7192242957174544 | > t_inv value:1.6526650592326861 means that it is significant by 0.05.
```
![output of the quick_look_two_data](https://github.com/montblanc18/statstester/tree/master/img/quick_look_two_data.png, "quick_look_two_data")

# License Information
See the file `LICENSE` for information on the history of this software.