#create a container called sum
#collect input from the user 


def number_in_String(first_user_input,second_user_input):
	
	value1 = int(first_user_input)
	value2 = int(second_user_input)
	result = str(value1 + value2)

	
	return result


user = input("Enter number")
user2 = input("Enter second number")
print(number_in_String(user,user2))
	