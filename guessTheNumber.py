#!/usr/bin/python3

import random, sys

target_num = random.randint(1, 20)
count = 0
while True:
	guess = int(input('Type your guess: '))
	count += 1
	if guess == target_num:
		print('You guessed correctly! It took you ' + str(count) + ' guesses.')
		sys.exit()
	if guess < target_num:
		print('You guessed ' + str(guess) + ', but it was too low.')
	if guess > target_num:
		print('You guessed ' + str(guess) + ', but it was too high.')
