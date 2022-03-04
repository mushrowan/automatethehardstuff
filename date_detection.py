#!/usr/bin/python3

import re
'''
Write a regular expression that can detect dates in the dd/mm/yyyy format. Assume that days range from 01-31, the months range from 01 to 12, and the eyars range from 1000 to 2999. Note that if the day or month is a single digit, it'll have a leading zero.
'''

date_detection_preprocessed = re.compile(r'''(
    
    (0[1-9]|[12][0-9]|3[01])
    \/
    (0[1-9]|1[0-2])
    \/
    ([12]\d\d\d)

)''', re.VERBOSE)

test_string = '29/02/2000'

test_output = date_detection_preprocessed.findall(test_string)

print(test_output)
output_is_valid = True
for match in test_output:
    day = match[1]
    month = match[2]
    year = match[3]

    if day == '29' and month == '02':
        if int(year) % 4 != 0:      # If year is not a leap year, there cannot be 29 days.
            output_is_valid = False
        elif int(year) % 100 == 0:  # If year is divisible by 100, there is no leap year.
            if int(year) % 400 == 0:# But if the year is divisible by 400, there is a leap year anyway. Lol.
                continue
            else:
                output_is_valid = False
    elif month == '02' and day in ['30', '31']:
        output_is_valid = False
    elif month in ['04', '06', '09', '11']:
        if day == '31':
            output_is_valid = False
    

print(output_is_valid)