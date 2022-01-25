#!/usr/bin/python3

sample_working_board = {'a2': 'bking', 'a3': 'wpawn', 'f4': 'wking'}
sample_broken_board1 = {'a2': 'bking'} # Only has one king
sample_broken_board2 = {'a9': 'bking', 'e4': 'wking'} # 'a9' isn't a board square




default_squares = [] 
for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    default_squares += [letter + str(int) for int in range(1, 9)]
# Check if all dictionary keys (squares) are in the list of default squares
print(list(sample_working_board.keys()))
if set(sample_working_board.keys()).issubset(default_squares):
    print('All keys are valid.')
else: 
    print('This ain\'t good, chief.')
print(default_squares)

