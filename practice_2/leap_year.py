#!/usr/bin/python
try:
 year = raw_input("Enter year\n")
 year = int(year)
 if (not year % 4 and year % 100) or not year % 400:
	print('Leap year')
 else:
	print('Normal year')
except (ValueError, TypeError):
    	print('invalid input') 
