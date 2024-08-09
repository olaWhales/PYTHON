def element_on_odd(index):
	number = 0
	for value in index:
		if(value %2 == 1):
			number = value
	return number
numbers = [1,2,3,4,5,6,7,78,9]
print(element_on_odd(numbers))
			