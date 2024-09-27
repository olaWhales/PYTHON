#create a variable named number 
#give it a value of 1000 
#create another variable called sum to add all integers together 
#create a loop to read integers
#use a variable sum to add all integers together
#print the result

def integer_addion(number):
	#number = 1000
	sum = 0
	for count in range (number):
		count+1
		sum = sum + count
	return sum
print(integer_addion(1000))