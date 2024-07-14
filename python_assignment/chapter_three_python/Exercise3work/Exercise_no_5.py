print("ENTER TWO NUMBERS FOR COMPARISON INTEGER AND OPERATOR")
first_user = int(input("Enter first number: "))
second_user = int(input("Enter second number: "))

if(first_user == second_user):
	print(first_user, "is equal to ", second_user)
else:
	print(first_user, "not equal to ", second_user)

if(first_user < second_user):
	print(first_user, "is lesser ", second_user)
else:
	print(first_user, "is greater than ", second_user)
	
if(first_user <= second_user):
	print(first_user, "less than and equal to ", second_user)
elif(first_user >= second_user):
	print(first_user, "greater than and not equal to ", second_user)
else:
	print(first_user, "not the same as " ,second_user)

