def arbitrary_argument(*args):
	number = 1
	for value in args:
		number*=value
	return number
print(arbitrary_argument(12,10,2))