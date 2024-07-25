def seconds_since_midnight(time):
	hour_in_seconds = 13 * 3600
	minute_in_seconds = 30 * 60
	seconds =  45
	
	result = hour_in_seconds + minute_in_seconds + seconds
	return result


print(seconds_since_midnight(136045))
