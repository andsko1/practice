#!/usr/bin/python
months = { "January": 1, "February": 2, "March": 3, "April": 4, "May": 5,
            "June": 6, "July": 7, "August": 8, "September": 9, "October": 10,
           "November": 11, "December": 12 }
try:
 ri = raw_input("Enter month\n")
 if months.has_key(ri):
	print 'Number month is', months[ri]
 else:
	print ('Invalid month name')
except (TypeError):
        print('Invalid input')

