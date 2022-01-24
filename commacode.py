#!/usr/bin/python3

spam = ['apples', 'bananas', 'tofu', 'cats']

print(str(enumerate(spam)))

def comma_code(input_list):
	output_string = ''
	if input_list == []:
		return 'You have inputted an empty list.'
	
	for index in range(len(input_list)):
		if index == len(input_list) - 1:
			output_string += (input_list[index] + '.')
		elif index + 1 == len(input_list) - 1:
			output_string += (input_list[index] + ' and ')
		else:
			output_string += (input_list[index] + ', ')
	return output_string

print(comma_code(spam))	
	# Check if there is an item 2 spaces on 
# 	comma_string = ''
# 	for index, item in enumerate(input_list):
# 		if input_list[in
	
		
