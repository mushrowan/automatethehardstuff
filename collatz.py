#!/usr/bin/python3

def collatz(number):
	try:
		number = int(number)
		if number == 1:
			print('We\'ve reached 1!')
		else:
			print(number)
		if number == 1:
			return True
		if number % 2 == 1:
			collatz(3 * number + 1)
		elif number % 2 == 0:
			collatz(number // 2)
	except ValueError:
		print('Invalid input. Please enter an integer.')
collatz(input('Please enter an integer to collatz it: '))	
