#!/usr/bin/python3

spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese) # note that the value has not changed - as it is an immutable data type, a new reference is created in the creation of the new 'spam' version - spam now refers to a 100 value in the commputer's memory.

butter = [0, 2, 4, 6, 8]
crackers = butter # the data type is immutable, so the reference is being copied, not the list.
butter[1] = 'Hello!' # this changes the list value.
print('butter is the following:')
print(butter)
print('crackers are the following:')
print(crackers) # the butter variable refers to the same list.

