def happy_house(number):
	if(number % 3 == 0 and number % 5 == 0):	
		return("happy_house")
	if(number % 3 == 0):
		return("happy")
	if(number % 5 == 0):
		return("house")
	else:
		return(number)
print(happy_house(30))