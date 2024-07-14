user_pass_input = 0
user_failed_input = 0
for count in range (11):
	grade = int(input("Enter your grade number(1=pass,2=fail)"))

	if (grade == 1):
		user_pass_input = grade
		user_pass_input = user_pass_input + 1
		print("passed student", user_pass_input)

	if (grade == 2):
		user_failed_input == grade
		user_failed_input = user_failed_input + 1
		print("failed student", user_failed_input)

print("Total pass student is: ",user_pass_input)
print("Total fail student is: ",user_failed_input)