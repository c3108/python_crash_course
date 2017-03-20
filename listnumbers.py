start_number = 1
end_number = 5

numbers = list(range(start_number,end_number))
squares = list(numbers)

for index in range(len(squares)):
	squares[index] **= 2

print(numbers)
print(squares)

# list of even numbers
print(list(range(2, 11, 2)))

squares_again = []
for value in range(1, 11):
	squares_again.append(value**2)

print(squares_again)


#Simple statistics list

digits = [1,2,3,4,5,6,7,8,9,0]
print("min digit = " + str(min(digits)))
print("max digit = " + str(max(digits)))
print("digit sum = " + str(sum(digits)))