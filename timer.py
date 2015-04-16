# 
# File: timer.py
# Author: Isaac J. Mertzenich
# (c) 2015
# Created: April 15, 2015
#
# Description: This file contains a timer that can be started Author
#at a certain time. This is used to keep track of the game clock, so
#as to determine when the game ends. This file works as a countdown.
#

#IMPORTS

import time

##################################################################################################################################

#METHODS


def minutesToSeconds(timeToConvert):

	minutes = timeToConvert
	
	seconds = minutes * 60

	return seconds





def countdown(obj, timeInMinutes):

	t = minutesToSeconds(timeInMinutes)

	print("Initialized: ", str(obj))
	
	while t:
		mins, secs = divmod(t, 60)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		print(str(obj), "=> Time Remaining: ", timeformat, end='\r')
		time.sleep(1)
		t -= 1

	print("Deinitialized: ", str(obj))


