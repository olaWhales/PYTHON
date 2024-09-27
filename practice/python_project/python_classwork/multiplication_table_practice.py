
print("Table2	","Table3	","Table4	","Table5	","Table6	","Table7	","Table8	","Table9	","Table10	")
for number in range(1, 13):	
	print(number * 2,'	',number * 3,'	', number *4,'	',number *5,'	',number *6,'	', number *7,'	',number *8,'	',number *9,'	',number *10)



for count in range(1, 12):
		#(' '):
	for counter in range(1, 12):
		count * counter
		print(f'{counter :<2} * {count:<2} = {count * counter : <4}', end=' ')
	