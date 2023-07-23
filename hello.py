# [11:26 AM] Santosh (Guest)

# Given an array A of integers and integer K. 
# return the maximum sum such that there exists 
# equation whose sum is less than K value, if not return -1


# Example 1:


# , K = 60

# import operator
# tuple(map(operator.add, a, b))
A = [34,23,1,24,75,33,54,8]
K = 60
# Printing the input
print("The original input is:", A)
 
# Using zip() function and list slicing
tup_list = list(zip(A[:-1], A[1:]))
for num in tup_list:
    print(num)
    print(num[0])
    print(num[1])
    left_side = num[0]
    right_side = num[1]
    tuple_sum = left_side + right_side
    print(f"sum: {tuple_sum}")
def tuple_value(tl):
    for num in tl:
        left_side = num[0]
        right_side = num[1]
        tuple_sum = left_side + right_side
        if tuple_sum > K:
            return -1
        return tuple_sum
result = tuple_value(tup_list)


  # iterate in each tuple element

# add_two_numbers = lambda result[0:], y: x + y 

# Handling the first and last elements

 
# Printing the result
print("The result is:", result)



# output: [34, 24]  value - 58




# Explanation

# We can use 34 and 24 to sum 58 which is less than 60 and there’s no par with sum of 59. Therefore, te maximum sum is 58

# Example 2:




Input: A = [10,61,20,30,40,50,54,68,32,24,23,34,58,72],




K = 85




K = 15


