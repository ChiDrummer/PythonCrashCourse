#looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here's the first three players on my team.")
for player in players[:3]:
	print(player.title())
	
print("\n")

#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy Friend's favorite foods are:")
print(friend_foods)

print("\n")

#copying a list with a modification
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy Friend's favorite foods are:")
print(friend_foods)
