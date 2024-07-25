from random import randint


number_generate = randint(1 , 1000)
yes = "yes"
no = "no"


while(super != "NO"):
	user = int(input("Guess my number between (1 - 1000)"))
	if (user < number_generate):
		print("Too low,Try again")
		
	if (user > number_generate):
		print("Too high>>>>")
		
	if (user == number_generate):
		print("Congratulation!!!!!!")
		user2 = input("Do you still want to guess again ? ENTER (YES) or (NO) to cancel")
		if (user2 == "YES"):

			user2 = input("Do you still want to guess again ? ENTER (YES) or (NO) to cancel")

			user = int(input("Guess my number between (1 - 1000)"))

	