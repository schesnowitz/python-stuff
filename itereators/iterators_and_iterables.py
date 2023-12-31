# -*- coding: utf-8 -*-
"""Iterators and Iterables.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vUzWXjsPNn5f-UAX8-N3cQ0y6hztsgB-
"""

nums = [1,2,3]
iter_nums = nums.__iter__()
print(iter_nums)
print(dir(iter_nums))
print(next(iter_nums))
print(next(iter_nums))

"""simply call iter method"""

nums = [1,2,3]
iter_nums = nums.__iter__()
print(iter(iter_nums)) #
print(dir(iter_nums))
print(next(iter_nums))
print(next(iter_nums))

"""iterator is an object with a state  -- remembers where it is during iteration"""

class Myrange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current_value = self.value
        self.value += 1
        return current_value



numbers = Myrange(1, 11)
print(next(numbers))
print(next(numbers))

for n in numbers:
    print(n)

def ranger(start, end):
    number = start
    while number < end:
        yield number
        number += 1


numbers = ranger(1, 11)
print(next(numbers))
print(next(numbers))

for n in numbers:
    print(n)

class Sentence:
    def __init__(self, sentence_data):
        self.sentence_data = sentence_data
        self.index = 0
        self.words = self.sentence_data.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


sentence = Sentence("Driver is my best buddy in ze world!")

for word in sentence:
    print((word))

def sentence_func(sd):
    sd = sd.split()
    for word in sd:
        yield word

sentence = sentence_func("Driver is my best buddy in ze world!")

for word in sentence:
    print((word))