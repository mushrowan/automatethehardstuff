#!/usr/bin/python3

def eggs(some_parameter):
	some_parameter.append('hello')

spam = [1, 2, 3,]
eggs(spam)
print(spam) # Even though spam and some_parameter contain separate references, they both refer to the same list.

import copy
spam = ['A', 'B', 'C', 'D']
print(id(spam))
cheese = copy.copy(spam)
id(cheese) # cheese is a completely different list with a different identity.
cheese[1] = 42
print(spam)
