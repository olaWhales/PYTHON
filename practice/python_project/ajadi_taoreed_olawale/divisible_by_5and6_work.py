# prompt the user to enter number
# check if the number is divisible by both 5 & 6
# check if the number is divisible by any of the number
# check if the number is divisible by one number but not both


number = int(input("Enter numbers"))
if(number % 5 == 0 and number % 6 == 0):
	print(True)
else:
	print(False)
if(number % 5 == 0 | number % 6 == 0):
	print(True)
else:
	print(False)
if(number % 5 == 0 | number % 6 == 0):
	print(True)
else:
	print("none")