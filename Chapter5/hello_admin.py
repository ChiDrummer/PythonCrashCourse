#write a differnt greating for admin user
usernames = ['eric', 'ken', 'beth', 'stacy', 'admin']

for username in usernames:
    if username == 'admin':
        print("Welcome, " + username.title() + ".  We've been waiting for you.\n")
    else:
        print("Successful login, " + username.title() + "!\n")

print("\n")

#write a program that maes sure each username is unique
current_users = ['george', 'tony', 'tina', 'jack', 'stephanie', 'jill', 'corey']

new_users = ['becky', 'rachel', 'tina', 'scott', 'jonny', 'erin', 'tony',]

for  new_user in new_users:
    if new_user in current_users:
        print(new_user.title() + ", is not an available username.\n")
    else:
        print("Welcome to the site, " + new_user.title() + "!\n")

