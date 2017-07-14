#basic if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
print("\n")

#conditional tests done in the CMD
car = 'Audi'
car.lower() == 'audi'

#checkig for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("HOld the ancohvies")
    
print('\n')

#checking not values in a list
banned_users = ['eric', 'ken', 'ben', 'davin', 'paul']

user = 'ken'
user = 'maria'

if user not in banned_users:
    print(user.title() + ", you are not on the Banned User List.  Welcome to the site!\n")

print("\n")


