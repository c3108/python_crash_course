print(list(range(1,21)))

million = list(range(1,1000001))

print("min million = " + str(min(million)))
print("max million = " + str(max(million)))
print("sum million = " + str(sum(million)))

odds = range(1,20,2)

for odd in odds:
	print(odd)

threes = range(3,31,3)
for three in threes:
	print(three)

cubes = [value**3 for value in range(1, 11)]
print(cubes)

print("The first three values of cubes are " + str(cubes[:3]))
print("The last three values of cubes are " + str(cubes[-3:]))