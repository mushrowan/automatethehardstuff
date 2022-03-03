#!/usr/bin/python3
from cgi import test
from distutils.filelist import findall
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

test_string = '29/02/2022'

test_output = date_detection_preprocessed.findall(test_string)

print(test_output)
output_is_valid = True
for match in test_output:
    day = match[1]
    month = match[2]
    year = match[3]
    if day == '28' and month != '02' or day == '29' and month != '02':
        output_is_valid = False
    
    if day == '28' and int(year) % 100 != 0:

print(output_is_valid)