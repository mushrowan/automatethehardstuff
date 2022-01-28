#!/usr/bin/python3
# Takes a list of lists of strings and displays them in a well-organised table with each column right-justified. Assumes that each inner list contains the same number of strings.

table_data = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['Dogs', 'cats', 'moose', 'goose']]


# Figure out the longest item in a string

def calculate_column_width(input_list):
    current_longest = 0
    
    for item in input_list:
        if len(item) > current_longest:
            current_longest = len(item)
    current_longest += 1 # Add one so that we always have at least 1 space
    return current_longest

sub_list_lengths = [] # This list will consist of the length of the longest strings in each list.
# sub_list_lengths[0] will be the longest length in table_data[0]. 

for sub_list in table_data:
    sub_list_lengths.append(calculate_column_width(sub_list))
print(sub_list_lengths)
    
for item in range(len(table_data[0])): # We assume that the length of the first column will be the same as the length of all of the columns
    row_string = ''
    for list_no in range(len(table_data)): # Compute each column once at a time. list_no is the index of the column. we want, e.g. 'apples alice dogs'
       row_string = row_string + table_data[list_no][item].rjust(sub_list_lengths[list_no])
    print(row_string)
