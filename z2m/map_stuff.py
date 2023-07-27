# -*- coding: utf-8 -*-
"""map.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xXyH4Q7RF9OETQqsW1RphwPxdLyRkZlu
"""

def mult_by_2(data_list):
    new_data_list = []
    for item in data_list:
        item = item * 2
        new_data_list.append(item)
    return new_data_list
print(mult_by_2([1,2,3,1,2,3]))

"""using map()  iterate without a loop"""

'''
map(func, *iterables) --> map object
Make an iterator that computes the function using arguments from
each of the iterables.  Stops when the shortest iterable is exhausted.
'''
def mult_by_2(data_list):
    # new_data_list = []  no need for this anymore as we take care of below
    # for item in data_list: map takes care of iteration
    # item = item * 2
        # new_data_list.append(item)
    return data_list*2
print(map(mult_by_2, [1,2,3,4]))
print(list(map(mult_by_2, [1,2,3,4]))) # covert to list
squared_numbers = list(map(lambda x: x ** 2, [1,2,3,4]))
print(squared_numbers)