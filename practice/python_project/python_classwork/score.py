for count in range (1,21):
	for index in [count]:
		if index % 2 == 0:
			result = [index]
			print(result)

numbers = list(range(1,21))

even_number = []
for number in numbers:
	if number %2 == 0:
		even_number.append(number)

print(even_number)


