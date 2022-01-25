#!/usr/bin/python3

sample_working_board = {'a2': 'bking', 'a3': 'wpawn', 'f4': 'wking'}
sample_broken_board1 = {'a2': 'bking'} # Only has one king
sample_broken_board2 = {'a9': 'bking', 'e4': 'wking'}




default_squares = [] 
for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    default_squares += [letter + str(int) for int in range(1, 9)]
print(default_squares)

