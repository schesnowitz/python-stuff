

# Given an array A of integers and integer K. 
# return the maximum sum such that there exists 
# equation whose sum is less than K value, if not return -1



A = [34, 23, 1, 24, 75, 33, 54, 8]
K = 50


tup_list = list(zip(A[0:], A[1:]))
print(tup_list)

def tuple_value(tl):
    print(len(tl))
    index = 0
    while index < len(tl):
        for num in tl:
            left_side = num[0]
            right_side = num[1]
            tuple_sum = left_side + right_side

            if tuple_sum > K:
                print(f"Greater than 50 {tuple_sum}")
            else: 
            # print(f"index count {index}")
            # print(f"tuple length {len(tl)}")
                print(f"Less than 50 {tuple_sum}")
            index += 1
tuple_value(tup_list)



import itertools as it

# num_iterations = int(input('How many? '))
# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         b = a+b
#         yield b
#         a = a+b

# for x in it.islice(fib(), num_iterations):
#     print(x)