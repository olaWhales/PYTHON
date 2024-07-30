#prompt user to enter number
#go through the number 
#if it's an even, print YES it's an even number 
#if it's an odd number, print it's an odd number


user = int(input("Enter a number: "))
if(user % 2 == 0):
	print("It's an even number")
if(user % 2 != 0):
	print("It's an odd number") 