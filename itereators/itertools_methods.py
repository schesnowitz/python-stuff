# -*- coding: utf-8 -*-
"""itertools.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OUZ9Lz-N1e3hYCd5Q5QF4PF1oA_FJgVg
"""
import itertools


counter = itertools.count()

print(next(counter))
print(next(counter))

some_data = ("Driver is my best buddy in ze world!").split()

# counter = itertools.count(some_data)

kv = zip(itertools.count(), some_data)

for i in kv:

    print(i)

some_data = ("Driver is my best buddy in ze world!").split()

counter = itertools.count(start=5, step=5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))



some_data = ("Driver is my best buddy in ze world!").split()


kv = itertools.zip_longest(range(10), some_data)

for i in kv:

    print(i)



some_data = ("Driver is my best buddy in ze world!").split()

counter = itertools.cycle(('On', 'Off'))

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))



some_data = ("Driver is my best buddy in ze world!").split()

counter = itertools.repeat(4, times=5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

squares = map(pow, range(15), itertools.repeat(2))

print(list(squares))



tup = [(0,2),(1,2),(2,2),(3,2),]

squares = itertools.starmap(pow, tup)

print(list(squares))



letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

# combinations order maters as in hand of cards K A is same as A K
# this method will only return one of these
result = itertools.combinations(letters, 2)

for i in result:
    print(i)

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]


letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

# this retuns ab and ba good for simulating outcome of a race for example
# this does not return repeats such as AA so not good for getting all possible combos

result = itertools.permutations(letters, 2)

for i in result:
    print(i)



letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

# all possible combinations

result = itertools.product(numbers, repeat=4)
count = 0
# for i, count in enumerate(result):
for i in result:
    count += 1
    print(i, count)




letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

# all possible combinations

result = itertools.combinations_with_replacement(numbers, 4)
count = 0
# for i, count in enumerate(result):
for i in result:
    count += 1
    print(i, count)