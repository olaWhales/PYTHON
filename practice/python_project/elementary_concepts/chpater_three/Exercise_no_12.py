user = int(input("Enter number from (5 integers): "))
number1 = user // 1 %10
number2 = user // 10 %10
number3 = user // 100 %10
number4 = user // 1000 %10
number5 = user // 10000 %10

if (number5 == number1 and number4 == number2):
	print("The number is a palindrome")
else:
	print("The number isn't a palindrome")