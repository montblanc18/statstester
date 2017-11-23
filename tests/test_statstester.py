#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import numpy.random
from statstester.statstester import *

class TestStats(unittest.TestCase):

    def test_coefficient_of_determination(self):
        x = numpy.random.rand(20)
        y = numpy.random.rand(20)
        _correlation_coefficient = sum( (x - np.mean(x)) * (y - np.mean(y))) / sum((x - np.mean(x))**2) / (sum((y - np.mean(y))**2))
        _coefficient_of_determination = _correlation_coefficient**2
        self.assertEqual(_coefficient_of_determination, coefficient_of_determination(x, y))
        

    def test_correlation_coefficient(self):
        x = numpy.random.rand(20)
        y = numpy.random.rand(20)
        _correlation_coefficient = sum( (x - np.mean(x)) * (y - np.mean(y))) / sum((x - np.mean(x))**2) / (sum((y - np.mean(y))**2))
        self.assertEqual(_correlation_coefficient, correlation_coefficient(x, y))
    
    def test_deviation_sum_of_products(self):
        x = numpy.random.rand(20)
        y = numpy.random.rand(20)
        _deviation_sum_of_products = sum( (x - np.mean(x)) * (y - np.mean(y)))
        self.assertEqual(_deviation_sum_of_products, deviation_sum_of_products(x, y))
        
    def test_sum_of_squared_deviations(self):
        x = numpy.random.rand(20)
        _sum_of_squared_deviations = sum((x-np.mean(x))**2)
        self.assertEqual(_sum_of_squared_deviations, sum_of_squared_deviations(x))

    
    def test_sxy(self):
        x = numpy.random.rand(20)
        y = numpy.random.rand(20)
        _sxy = sum(( x - np.mean(x)) * (y - np.mean(y)))
        self.assertEqual(_sxy, sxy(x, y))
    
    def test_syy(self):
        y = numpy.random.rand(20)
        _syy = sum((y-np.mean(y))**2)
        self.assertEqual(_syy, syy(y))

    def test_sxx(self):
        x = numpy.random.rand(20)
        _sxx = sum((x-np.mean(x))**2)
        self.assertEqual(_sxx, sxx(x))
        

    def two_line_t_test():
        """ 今後実装予定
        """
        pass


    def test_t_test(self):
        x = [68, 75, 80, 71, 73, 79, 69, 65]
        y = [86, 83, 76, 81, 75, 82, 87, 75]
        t, p = t_test(x, y)
        self.assertEqual(t, -3.2140431468219668)
        self.assertEqual(p, 0.0062436950143002282)
        t, p = t_test(x, y, equal_var = False)
        self.assertEqual(t, -3.2140431468219668)
        self.assertEqual(p, 0.0063061781663365105)
        
    def test_f_test(self):
        x = [10, 23, 19, 14, 41, 33, 36, 31, 50]
        y = [14, 84, 44, 11, 36, 71, 34, 54, 61]
        self.assertEqual(0.046638962563471921, f_test(x, y))
