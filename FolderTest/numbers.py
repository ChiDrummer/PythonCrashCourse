#using the range() function
for value in range(1,5):
	print(value)



for value in range(1,6):
	print(value)



#using range to make a list of numbers 
numbers = list(range(1,6))
print(numbers)

print("\n")

#even numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

print("\n")

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
	
print(squares)
print("\n")

#list comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)

