#prompt user to enter three integer
#check the first number by dividing by 1 and modulo to get the remainder
#check the second number by dividing by 10 and modulo to get the remainder
#check the first number by dividing by 100 and modulo to get the remainder
#compare the first number with the last number if both are the same (it's says, it's a pallindrome(TRUE)) and if not the same (means not a pallindrome(FALSE))


def reverse(number):
	user1 = number // 1 %10
	user2 = number // 10 %10
	user3 = number // 100 %10

	if(user1 == user3):
		return True
	else:
		return False
print(reverse(454))