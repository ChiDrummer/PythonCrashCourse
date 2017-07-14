#ordering lists with sort and reverse
world = ['france', 'germany', 'austra', 'england']

print("List in original order:")
print(world)

print("\nList in sortED order:")
print(sorted(world))

print("\nList still in original order:")
print(world)

print("\nList in reverse alphabet order:")
world_sorted = sorted(world, reverse=True)
print(world_sorted)

#cant figure out how to print a reverse alphabitized list using sortED

print('\nWatch This\n')

for place in world_sorted:
	print(place)



