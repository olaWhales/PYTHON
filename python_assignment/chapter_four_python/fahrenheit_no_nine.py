def fahrenheit_no_nine(ceisus):
	temperature = (9/5 * ceisus) + 32
	return temperature
for ceisus in range(1,101):
	print(fahrenheit_no_nine(ceisus))
	