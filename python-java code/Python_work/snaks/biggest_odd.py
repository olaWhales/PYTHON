def biggest(number):
	numbers = number.split()
	integer_list = [int (num) for num in numbers]
	odd_numbers = [num for num in integer_list if num % 2 != 0]
	if odd_numbers:

		return max(odd_numbers)






number =input("Enter number seperating with a space: ")
result = biggest(number)
print (result)

	






