#!/usr/bin/python3

import random
number_of_streaks = 0
for experiment_number in range(10000):
	# Create a list of 100 'heads' or 'tails' values:
	flip_list = []
	h_counter = 0
	t_counter = 0	

	for flip_number in range(100):
		flip = random.randint(0, 1)
		if flip == 0:
			flip_face = 'H'
			h_counter += 1
			t_counter = 0	
		elif flip == 1:
			flip_face = 'F'
			t_counter += 1
			h_counter = 0
		flip_list.append(flip)
		if h_counter == 6 or t_counter == 6:
			number_of_streaks += 1
			break			
print(number_of_streaks)
print('Chance of streak: %s%%' % (number_of_streaks / 100))
