alien_colors = ["Green", "Green", "Blue", "Red", "yellow"]

count_points = 0

for alien_color in alien_colors:
	if alien_color.lower() == "green":
		print("You earned 5 points!")
		count_points += 5
	elif alien_color.lower() == "yellow":
		print("You did great, 15 points!")
		count_points += 15
	else:
		print("10 points for you!")
		count_points += 10

print("You won " + str(count_points) + " points!")