# -*- coding: utf-8 -*-
"""reduce.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_vHDupyQOP8Eik7fAkTTSDfhofWh2OuD

reduce()
"""

from functools import reduce
nums = [1,10,2,20]

def some_func(argu, item):
    return argu + item


# takes in function, data, initial value
r = reduce(some_func, nums, 0)
print(r)
