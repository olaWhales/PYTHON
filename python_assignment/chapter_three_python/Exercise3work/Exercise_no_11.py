length_of_miles = 0
gallon_used = 0
total_used = 0
travel = 0
driver_input = float(input("Enter the amount of gallon used: "))
driver2_input = int(input("Enter the miles driven: "))

while(driver_input != -1):

	driver_input = float(input("Enter the amount of gallon used: "))
	driver2_input = int(input("Enter the miles driven: "))
	
	length_of_miles = length_of_miles + driver_input 
	gallon_used = gallon_used + driver2_input
		
	total_used = (gallon_used / length_of_miles)
	
	driver_input += travel
	print("The mile/per gallon used is : ", total_used)
print("The overall total mile/per gallon is used: ", total_used)