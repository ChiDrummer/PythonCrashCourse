#use program from chapterto do the following:
#print message and print slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)

print("Here's the first three items from the list:")
for player in players[0:3]:
	print(player.title())
	
print("\n")

print("Here's the middle three items from the list:")
for player in players[1:4]:
	print(player.title())
	
print("\n")

print("Here's the last three items from the list:")
for player in players[2:]:
	print(player.title())
