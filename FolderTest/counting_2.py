#use third arguement to list odd numbers to 20
for value in range(1,20,2):
	print(value)
print("\n")

#make a list of the multiples of 3.  print for loop
for value in range(3,31,3):
	print(value)
print("\n")

#print a list of the cubed integers from 1 to 10
cubed = []
for value in range(1,11):
	cube = value**3
	cubed.append(cube)
	
print(cubed)
print("\n")

#same exersize using list comprehension
cubed = [value**3 for value in range(1,11)]
print(cubed)
print("\n")



	
	

