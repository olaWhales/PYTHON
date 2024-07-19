fail =0
pass =0
for student in range(1,16):
	score = int(input("Enter scores: "))
	if (score == 45):
		pass = score
		pass = pass + 1
	else (score < 45):
		fail = score
		fail = fail + 1	
print("The pass students: ",pass)
print("The fail students: ", fail)