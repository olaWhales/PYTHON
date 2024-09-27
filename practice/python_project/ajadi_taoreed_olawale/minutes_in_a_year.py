#create a variable called minute_in_a_year and give it value
#create a variable named minutes_in_a_day and give it a value
#create a variable names minutes in a year
#collect input from user named user_input  
#divide the user input by the minutes in a year to get the number of the years
#multiply the number of year by the minute_in_a_year and subrtract from the original number from the user to get the number of days   

def minutes_in_a_year(result):
	days_in_a_year = 365
	minutes_in_a_day = 1440
	minute_in_a_year = 259200
	break_input_by_minutes = user_input // minute_in_a_year
	return break_input_by_minutes
	days = break_input_by_minutes * (days_in_a_year - user_input)
	return days
	

user_input = int(input("Enter the minutes to calculate: "))
print(minutes_in_a_year(user_input))