# -*- coding: utf-8 -*-
"""performance_decorator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xahRjTeksP7zapvOGcc0KAgAganl-wBP
"""

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        total_time = end_time - start_time
        print(f"Run Time = {total_time}")
        return result
    return wrapper



@performance
def long_run_func():
    for i in range(100000000):
        times_5 = i*10000
    return times_5

long_run_func()