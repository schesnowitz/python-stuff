lst = [9,8,6,7,4,5,2,3,1,0]

sorted_lst = sorted(lst)
 
print(sorted_lst)

# or to sort original 
lst.sort()
print(lst)

sorted_lst = sorted(lst, reverse=True)
 
print(sorted_lst)

# or to sort original 
lst.sort(reverse=True)
print(lst)



tup = (9,8,6,7,4,5,2,3,1,0)

sorted_tup = sorted(tup)
 
print(sorted_tup)


my_dict = {'name': ['John', 'Doe'], 'age': [30, 40], 'address': ['123 Main Street', '456 Elm Street']} 

sorted_dict = sorted(my_dict)
# print(dir(sorted_dict))

for key, value in sorted(my_dict.items()):
    print(key, value)


# get absolute value
#
nums = [-1,-2,-6,5,7,9]    

sorted_abs = sorted(nums, key=abs)
print(sorted_abs)
