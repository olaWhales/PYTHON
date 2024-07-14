balance = 0
bank = ""
sentinel = 0
while bank != sentinel:
	bank = int(input('Welcome to our bank press 1 to deposit and 2 to withdraw:'))
	match bank:

			
		case 1:
			deposit = int(input("Enter amount to deposit:  "))
			balance = balance+deposit
			print("Your balance is: ",balance)
		case 2:
			withdraw = int(input("Enter amount to withdraw:  "))
			balance = balance-withdraw
			print("After withdrawer,your balance is:  ",withdraw)


