# -*- coding: utf-8 -*-
"""decorators_py.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_0qPoHn63cOH-RLtYepS7oyAyCoh3LJf
"""

def a_decorator(arg_in):
    def wrapper_function():
        print('wrapper function')
        arg_in()
        print('arg_in')
    return wrapper_function


def greeting():
    print("Hello Steve")
# greeting()
response = a_decorator(greeting) # this is what is happening
# if we print response we get the object...
response()  # we call it

"""as a decorator..."""

def a_decorator(arg_in):
    def wrapper_function():
        print('wrapper function')
        arg_in()
        print('arg_in')
    return wrapper_function

@a_decorator
def greeting():
    print("Hello Steve")

greeting()



def a_decorator(arg_in):
    def wrapper_function(hello):
        print('wrapper function')
        arg_in(hello)
        print('arg_in')
    return wrapper_function

@a_decorator
def greeting(hello):
    print(hello)

greeting("this text reps the hello argument")

"""calling with arg and kwargs"""



def a_decorator(arg_in):
    def wrapper_function(*args, **kwargs):
        print('wrapper function')
        arg_in(*args, **kwargs)
        print("********")
    return wrapper_function

@a_decorator
def greeting(hello, key1="Steve"):
    print(hello, key1)

greeting("hello")