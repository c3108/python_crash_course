start_number = 1
end_number = 5

numbers = list(range(start_number,end_number))
squares = list(numbers)

for index in range(len(squares)):
	squares[index] **= 2


print(numbers)
print(squares)

