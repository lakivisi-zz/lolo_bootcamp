def fizz(n):
	''' Returns fizz when a number is divisible by 3
	Returns buzz when a number is divisible by 5
	Returns fizzbuzz when a number is divisible by both 3 and 5
	'''


	if n % 3 == 0 and n % 5 == 0:
		return 'FizzBuzz'
	elif n % 5 == 0:
		return 'Buzz'
	elif n % 3 == 0:
		return 'Fizz'
	else:
		return n 