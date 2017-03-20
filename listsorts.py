places = ['Italy', ' Spain', 'France', ' Istanbul', 'egypt ']

#Clean up the data so that the cases and spacing are the same
for index in range(len(places)):
	places[index] = places[index].strip().title()

#Show that the sorted function does not modify the original list
print(sorted(places))
print(places)

#Show that sort() modifies the original list
places.sort()
print(places)

#demo revers() 
places.reverse()
print(places)

#demo len()
print("There are " + str(len(places)) + " people invited to dinner.")