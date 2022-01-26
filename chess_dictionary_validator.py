#!/usr/bin/python3

sample_working_board = {'a2': 'bking', 'a3': 'wpawn', 'f4': 'wking'}
sample_broken_board1 = {'a2': 'bking'} # Only has one king.
sample_broken_board2 = {'a9': 'bking', 'e4': 'wking'} # 'a9' isn't a board square.

possible_pieces = ['wking', 'wqueen', 'wrook', 'wbishop', 'wknight', 'wpawn', \
        'bking', 'bqueen', 'brook', 'bbishop', 'bknight', 'bpawn'] # All the possible pieces so that we can loop over them.

possible_squares = []
for letter in 'abcdefgh':
    possible_squares += [letter + str(int) for int in range(1, 9)] # Builds the list of ranks

def checkSquares(input_board, legal_board): # Input a legal list of squares. We'll probably want to use possible_squares.
    if set(input_board.keys()).issubset(legal_board): # Check that all the keys in a dictionary are in our list of legal squares.
        print('All keys are valid.')
        return True
    else:
        print('This ain\'t good, chief.')
        return False

def checkQuantities(input_board, piece_to_check): # Count the quantity of a given piece, given a board.
    count = 0
    for square, square_contents in input_board.items():
        if square_contents == piece_to_check:
           count += 1
    return count

def checkBoard(input_board, legal_squares): # Check a board.
    valid_board_flag = True # Flip this flag to False if something invalid is detected. This way we can detect all possible errors even if the first check results in an error.
    if checkSquares(input_board, legal_squares) == False:
        print('Some of the board keys are not valid.')
        valid_board_flag = False
    if checkQuantities(input_board, 'wpawn') > 8 or checkQuantities(input_board, 'bpawn') > 8:
        print('The input board has too many pawns.')
        valid_board_flag = False
    if checkQuantities(input_board, 'wking') != 1 or checkQuantities(input_board, 'bking') != 1:
        print('White and Black need to have exactly one king each.')
        valid_board_flag = False
    # ToAdd: Check if a pawn is on the 1st or 8th rank.
    if valid_board_flag == True:
        print('The board is valid!')
    return valid_board_flag
print(possible_squares)

print('Checking sample_broken_board1')
print(checkBoard(sample_broken_board1, possible_squares))

print('Checking sample_broken_board2')
print(checkBoard(sample_broken_board2, possible_squares))

print('Checking sample_working_board')
print(checkBoard(sample_working_board, possible_squares))
