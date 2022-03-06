import re
'''Write a function that does the same as the strip() function.
If no arguments are passed, whitespace characters should be removed.
'''


test_string = ' hi hello '

def regexStrip(input_string):
    arg = input('Enter text to be stripped off. Leave blank to strip whitespace.')
    if arg == '':
        arg = r'\s*'
        strip_regex = re.compile(r'^' + arg + r'(.+?)' + arg + r'$')
    else:
        arg = re.escape(arg)
        
        strip_regex = re.compile(r'^' + arg + r'(.+?)' + arg + r'$')
        

    result = strip_regex.search(input_string)
    return result.group()
print(regexStrip(test_string))

