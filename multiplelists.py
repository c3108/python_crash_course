# Pizza Topping Book example
# requested_toppings = ['onion', 'pepperoni', 'green peppers', 'cheese', 'sauce']
# available_toppings = ['pepperoni', 'sausage', 'chicken', 'cheese', 'sauce', 'olives']

# for requested_topping in requested_toppings:
# 	if requested_topping in available_toppings:
# 		print("Adding " + requested_topping + ".")
# 	else:
# 		print("Sorry, we don't have " + requested_topping + ("."))

#User Name Admin Example
user_names = ['Fred', 'George', 'Frank', 'kelly', 'Admin', 'kt177']
new_users = ['fred', 'crystal', 'carol', 'kelly']

if user_names:
	for user_name in user_names:
		if user_name.lower() == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello, " + user_name + " thank you for logging in again.")
else:
	print("We need to find some users!")

for new_user in new_users:
	for user_name in user_names:
		if new_user.lower() == user_name.lower():
			print("Sorry, " + new_user + ", name taken.")
		else:
			print(new_user + (", welcome to the club!"))

# Exercise 5-11 ordinal numbers
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print(str(number) + "nd")
	elif number == 3:
		print(str(number) + "rd")
	elif number >= 4:
		print(str(number) + "th")