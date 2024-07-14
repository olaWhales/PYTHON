
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))
if (first_number < second_number & third_number):
	print(first_number, " First number is the smallest number.")
if (second_number < first_number & third_number):
	print(second_number, " Second number is the smallest number.")
if (third_number < first_number & second_number):
	print(third_number, " Third number is the smallest number.")
if (first_number > second_number & third_number):
	print(first_number, " First number is the largest number.")
if (second_number > first_number & third_number):
	print(second_number, " Second number is the largest number.")
if (third_number > first_number & second_number):
	print(third_number, " Third number is the largest number.")
sum = first_number + second_number + third_number
print("The sum of all numbers is: ",sum)
average = sum / 3
print("The average number is: ",average)
multiply = first_number * second_number * third_number
print("The muiltiples of number is: ",multiply)

