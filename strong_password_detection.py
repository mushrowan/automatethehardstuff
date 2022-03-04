#!/usr/bin/python3

import re
'''
Strong password has:
1. 8 characters minimum
2. Uppercase and lowercase
3. Has at least 1 digit.

'''
minimum_characters_regex = re.compile(r'''
    \s
    .*
    .{8}
    .*
    \s
''', re.VERBOSE)

uppercase_and_lowercase_regex = re.compile(r'.*([a-z].*[A-Z]+|[A-Z].*[a-z]+).*')

has_digit = re.compile(r'.*\d.*')