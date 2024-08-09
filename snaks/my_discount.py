def my_discount(price,discount):
	discount = 0.15
	result = price * discount
	total = price - result
	return (total)


print(my_discount(200,10))
