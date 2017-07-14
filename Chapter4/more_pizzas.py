#take the pizza list, add items, print in a for loop for two lists
pizzas = ['sausage', 'pepperoni', 'mushroom', 'green pepper', 'cheese', 'black olive', 'pineapple', 'tacco', 'mustard']
friend_pizzas = pizzas[:]

pizzas.append('anchovi')
friend_pizzas.append('bbq')

print("My favorite foods are:")
for pizza in pizzas:
	print(pizza)

print("\nMy Friend's favorite foods are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
	
print("\n")

#take other exerzizes from this chapter and print in for loop
musics = ['clasical', 'jazz', 'rock', 'country']
friend_musics = musics[:]

musics.append('rap')
friend_musics.append('soul')

print("My favorite types of music are:")
for music in musics:
	print(music)
	
print("\nMy friend's favorite types of music are:")
for friend_music in friend_musics:
	print(friend_music)

