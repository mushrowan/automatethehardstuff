#!/usr/bin/python3

import time, sys
indent = 0 # How many spaces to indent.
indent_increasing = True # Whether the indent is increasing

try:
	while True: # The main programme loop.
		print(' ' * indent, end='')
		print('********            ********           ********')
		time.sleep(0.008) # Pause for 1/10 of a second.

		if indent_increasing:
			# Increase the number of spaces:
			indent += 1
			if indent == 20:
				# Change direction.
				indent_increasing = False
		else:
			# Decrease the number of spaces:
			indent -= 1
			if indent == 0:
				# Change direction.
				indent_increasing = True
except KeyboardInterrupt:
	sys.exit()
