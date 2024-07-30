def reverse(number):
	user1 = number // 1 %10
	user2 = number // 10 %10
	user3 = number // 100 %10

	if(user1 == user3):
		return True
	else:
		return False
print(reverse(454))