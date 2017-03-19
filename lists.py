names = ['jared', ' OWEN ', 'freD', 'george ', 'frank', 'ed']

names.append('crystal')
names.insert(2, 'amanda')

print("Goodbye!")

absent = names.pop(0)

print(absent.title().strip() + " can't make it anymore :-(.")

for name in names:
	print(name.title().strip() + " can make it to the party.")