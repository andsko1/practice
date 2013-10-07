#!/usr/bin/python
import math
const = {'pi': math.pi, 'e': math.e, 'y': 0.57721566490153286060651209008240243}
print ('Constants:')
print const.keys()
try:
 ri = raw_input("Enter constant and accuracy like cons:acc:")
 cons, acc = ri.split(':')
 if const.has_key(cons):
	print "%.{0}f".format(acc) % const[cons]
 else:
	print ('Is not constant')
except (ValueError, TypeError):
        print('Invalid input')

