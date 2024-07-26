#declare the area of Πr2 which is constant multiply by 2
#multiply the area by the length giving
#print the result(volume)


def area_of_circumferences(length):
	area = 3.14159 * 2
	volume = area * length
	return volume
print(area_of_circumferences(15))