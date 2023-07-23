import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3] 
names = ['Steve', 'Driver']
selectors = [True, True, False, True, True]
# 1 is start 5 is stop then step value 
result = itertools.islice(range(100),1, 5, 2)

for item in result:
    print(item)


with open('testlog.log', 'r') as f:
    header = itertools.islice(f, 3)

    for h in header:
        print(h)   


# returns coresponding data where selectors is true
result = itertools.compress(letters, selectors=selectors)

for item in result:
    print(item)



# using filter function as a comparison

def filt_func(n):    
    if n < 2:
        return True
    return False
print("filter--------")
result = filter(filt_func, numbers)
for item in result:
    print(item)
print("filter false--------")
result = itertools.filterfalse(filt_func, numbers)
for item in result:
    print(item)



print("drop WHILE--------")
# drops the first items that meet conditions 
# but then returns everything moving forward
numbers = [0, 1, 2, 3, 2, 1, 2,0] 
result = itertools.dropwhile(filt_func, numbers)
for item in result:
    print(item)
print("take while--------")

numbers = [0, 1, 2, 3, 2, 1, 2,0] 
result = itertools.takewhile(filt_func, numbers)
for item in result:
    print(item)

print("accumulate--------")


# running total
numbers = [0, 1, 2, 3, 2, 1, 2,0] 
result = itertools.accumulate(numbers)
for item in result:
    print(item)

print("accumulate multiply--------")
import operator

# running total multipy
numbers = [1, 2, 3, 2, 1, 2,0] 
result = itertools.accumulate(numbers, operator.mul)
for item in result:
    print(item)

print("group by--------")

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

# needs to tell groupby what to group by
# needs to be sorted before hand
def get_state(person):
    return person['state']

ps = itertools.groupby(people, get_state)


for key, group in ps:
    print(key) 
    for person in group:
        print(person)

print("groupby with counting objects--------")

ps = itertools.groupby(people, get_state)
for key, group in ps:
    print(key, (len(list(group)))) 


print("replicate iterator with tee--------")

ps = itertools.groupby(people, get_state)
cpy1, cpy2 = itertools.tee(ps)

for key, group in cpy1:
    print(key, (len(list(group)))) 