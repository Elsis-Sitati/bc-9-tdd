def fizz_buzz(number):
	if not number % 3  and not number % 5:
		return 'FizzBuzz'

	elif not number % 3:
		return 'Fizz'

	elif not number % 5:
		return 'Buzz'
		
	else:
		return number