largest = 0
smallest = 0
average = 0
product = 1
sum = 0
number_of_value = 4



for count in range (0, 4):
	value = int(input("Enter 3 value: "))

	if (smallest == 0 or value < smallest):
		smallest = value
	if (value > largest):
		largest = value
	sum = sum + value
	average = sum / number_of_value
	product = product * value


print("The lowest value is : ",smallest)
print("The largest value is : ",largest)
print("The sum of all value is : ",sum)
print("The average value is : ",average)
print("The product of the value is : ",product)