for i in range(1, 101):
	if i % 3 == 0:
		print(f"Fizz {i}")
	if i % 5 == 0:
		print(f"Buzz {i}")
	if i % 3 and i % 5 == 0:
		print(f"FizzBuzz {i}")