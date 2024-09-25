ten_percent_rate = 10
fifteen_percent_rate = 15
twenty_percent_rate = 20
twenty_five_percent_rate = 25

print("Wellcome!!! let's check your TAX-RATE")
price = input("Enter your name: ")

while(price != 'close'):

	price = int(input("Enter the price of your car:  "))

	if(price <= 1_000_000):
		ten_percent = price * (ten_percent_rate / 100)
		print(ten_percent)
	if(price > 1_000_000 & price <= 3_000_000 ):
		fifteen_percent = price* (fifteen_percent_rate / 100)
		print(fifteen_percent)
	if(price > 3_000_000 & price <= 5_000_000):
		twenty_percent = price * (twenty_percent_rate /100)
		print(twenty_percent)
	if(price > 5_000_000):
		twenty_percent = price * twenty_five_percent_rate / 100
		print(twenty_perent)
	else:
		print("Enter close to end program for the day  ")
	
