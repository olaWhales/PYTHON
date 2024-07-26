def arbitrary_argument(*args):
	number = 1
	for value in args:
		value = *number
	reteun value
print(arbitrary_argument(12,10))