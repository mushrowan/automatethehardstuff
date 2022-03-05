#!/usr/bin/python3

import re
'''
Strong password has:
1. 8 characters minimum
2. Uppercase and lowercase
3. Has at least 1 digit.

'''
test_input = 'MattBellamy0!!'
minimum_characters_regex = re.compile(r'.*.{8}.*')

uppercase_and_lowercase_regex = re.compile(r'.*([a-z].*[A-Z]+|[A-Z].*[a-z]+).*')

has_digit = re.compile(r'.*\d.*')


is_secure = False
if minimum_characters_regex.fullmatch(test_input):
    print('Minimum characters reached!')
    if uppercase_and_lowercase_regex.fullmatch(test_input):
        print('Has uppercase and lowercase!')
        if has_digit.fullmatch(test_input):
            print('has at least one number in it!')
            is_secure = True

print(is_secure)