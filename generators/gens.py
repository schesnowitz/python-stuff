def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result
    
some_nums = square_numbers([1,2,3,4,5,6,7,8,9,10])
# print(some_nums)

# as a generator
def square_numbers(nums):
    for i in nums:
        yield(i*i)

    
some_nums = square_numbers([1,2,3,4,5,6,7,8,9,10])
# print(next(some_nums))
# print(next(some_nums))
# print(next(some_nums))
# print(next(some_nums))
# will throw a  StopIteration error if nothing left to interate over

# so needs try except
# or
# for n in some_nums:
    # print(n)
