buffet = ("eggs", "bacon", "pancakes", "toast", "cereal")
 
print("Original Menu:")
for food in buffet:
	print("\t" + food)

buffet = ("eggs", "bacon", "pancakes", "muffins", "bagel")

print("\nModified Menu:")
for food in buffet:	
	print("\t" + food)

#New variable to count how many foods are bacon
not_bacon = 0

#Loop through the foods in buffet, and see if there is bacon.
for food in buffet:
	if food == "bacon":
		print("woohoo, bacon!")
	else:
		not_bacon += 1

print("There are " + str(not_bacon) + " foods that are not bacon :-(")

#using "in" instead of for loop to check for bacon
if "bacon" in buffet:
	print("Woohoo!!!! bacon!")
