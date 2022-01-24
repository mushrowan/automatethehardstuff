#!/usr/bin/python3

def spam(divide_by):
	try:
		return 42 / divide_by
	except ZeroDivisionError:
		print('Error: invalid argument.')	
print(spam(0))
print(spam(76))

