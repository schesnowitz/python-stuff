# -*- coding: utf-8 -*-
"""FunctionalProgramming.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C3jMeKPZrOgUPRM0jBAmAZjbPkMdzIMy

map()
"""

def mult_by_2(lst):
    multed_list = []
    for n in lst:
        multed_list.append(n * 2)
    return multed_list

response = mult_by_2([2,4,6])
print(response)


# using map()

def mult_by_2_map(lst):
    return lst * 2

response = list(map(mult_by_2_map, [2,4,6]))
print(response)

"""filter()"""

n_list = [2,4,6,7,9]
def get_odd_numbers(data):
    odd_numbers = []
    for d in data:
        if d % 2 != 0:
            odd_numbers.append(d)
    return odd_numbers
response = get_odd_numbers(n_list)
print(f"regular function: {response}")
# filter()

def filter_odd_numbers(data):
    return data % 2 != 0
response = list(filter(filter_odd_numbers, n_list))
print(f"filter function: {response}")

"""zip()"""

list_even = [2,4,6,8,10]
list_odd = [1,3,5,7,9]

response = list(zip(list_odd, list_even))
print(response)

list_of_nums = [1,1,5,5,10,10]
response = list(zip(list_of_nums))
print(response)

"""add adjacent"""

list_of_nums = [1,1,5,5,10,10]

print("The original list is : " + str(list_of_nums))

# using for loop to compute consecutive overlapping summation
length = len(list_of_nums)
# res = [test_list[i] + test_list[(i+1) % n] for i in range(n)]

# printing result
# print("The Consecutive overlapping Summation : " + str(res))

# response = list(zip(list_of_nums))
# print(response)

lst = [1,2,3,4,5,6,7,8,9,10]

count = 0

for i in lst:
    count = count + i
print(count)