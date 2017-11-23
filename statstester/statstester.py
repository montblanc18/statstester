#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import numpy as np
from scipy import stats


def coefficient_of_determination(x, y):
    r = correlation_coefficient(x, y)
    return r**2


def correlation_coefficient(x, y):
    r = sxy(x, y)/ sxx(x) / syy(y)
    return r


def deviation_sum_of_products(x, y):
    if len(x) != len(y):
        try:
            raise Exception
        except:
            pass
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    _deviation_sum_of_products = sum((x - x_mean) * (y - y_mean))
    return _deviation_sum_of_products


def sum_of_squared_deviations(x):
    """ xの偏差平方和を返す
    """
    return deviation_sum_of_products(x, x)


def sxy(x, y):
    """ xとyの偏差積和を返す
    """
    return deviation_sum_of_products(x, y)
    

def syy(y):
    """ リストyの偏差平方和を返す
    """
    return sum_of_squared_deviations(y)


def sxx(x):
    """ リストxの偏差平方和を示す。
    """
    return sum_of_squared_deviations(x)


def two_line_t_test():
    """ 2つのデータのアイデに相関があるかどうかを調べる。
    x0, y0: 比較元データ列。
    x1, y1: 比較先データ列。
    """

    """ 今後実装予定
    """
    pass
    
    

def t_test(x, y, equal_var = True):
    """ t検定を行う。
    指定がなければ、全ては等しい分散として扱う。
    t値とp値（確率）を返す。
    """
    return stats.ttest_ind(x, y, equal_var = equal_var)

def f_test(x, y):
    """ f検定を行う。
    """
    f = np.var(x)/np.var(y)
    return stats.f.cdf(f, len(x)-1, len(y)-1)
    

