#!/usr/bin/python3

my_pets = ['Oscar', 'Emmy', 'Bafta']
print('Enter a pet name:')
name = input()
if name not in my_pets:
	print('I do not have a pet named ' + name)
else:
	print(name + ' is my pet.')

cat = ['fat', 'grey', 'loud']
size, colour, disposition = cat
for index, item in enumerate(cat):
	print('Feature ' + str(index) + ' of a cat is that it is ' + item + '.')

