#!/usr/bin/python3

while True:
	print('Please type your name.')
	name = input()
	if name == 'your name':
		break
print('Thank you!')

while True:
	print('Who are you? (you are Joe, lol)')
	name = input()
	if name != 'Joe':
		continue
	print('Hello, Joe. What is the password? (It is a fish.)')
	password = input()
	if password == 'swordfish':
		break
	print('Access granted.')


print('My name is')
for i in range(5):
	print('Jimmy Five Times (' + str(i) + ')')

