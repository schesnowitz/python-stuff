work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

work_days.sort(reverse=True)
print(work_days)


numbers = [1, 11, 115, 13, 1305, 43]

numbers.sort(reverse=True)
print(numbers)

a = sorted(numbers, reverse=True)
print(a)

letters = ['a', 'A', 'abc', 'ABCca', 'aBcc','acesdfsee',  'aaaaBC', 'aaAbbc']
letters.sort(key=len, reverse=True)
print(letters)
letters.sort(key=str.lower)
print(letters)

a_copy = letters[:]
a_copy.sort(key=len, reverse=True)
print(a_copy)

a = sorted(a_copy, key=len, reverse=True)
print(a)
