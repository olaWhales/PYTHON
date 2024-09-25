def modified_average_function_no_six(*args):
	number = 1
	for value in args:
		number = number*value
	return number
print(modified_average_function_no_six(10,2,20,5))