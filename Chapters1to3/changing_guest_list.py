#start with last code.  one guest cant make it.  thikn of someone else to invite and resend invites.
din_guests = ['huyen', 'sarah', 'hilary']
print(din_guests)

message_0 = din_guests[0].title() + ", woud you like to go to dinner?"
message_1 = din_guests[1].title() + ", woud you like to go to dinner?"
message_2 = din_guests[2].title() + ", woud you like to go to dinner?"

print(message_0)
print(message_1)
print(message_2)

popped_guest = din_guests.pop(1)
print(popped_guest.title())

din_guests.insert(1, 'rachael')

message_0 = din_guests[0].title() + ", woud you like to go to dinner?"
message_1 = din_guests[1].title() + ", woud you like to go to dinner?"
message_2 = din_guests[2].title() + ", woud you like to go to dinner?"

print(message_0)
print(message_1)
print(message_2)

#next exersize - more people coming.  add them to specific places in the list

message = "More people are coming.  New invitations on the way!"
print(message)

din_guests.insert(0, 'steve')
din_guests.insert(2, 'greg')
din_guests.insert(4, 'mike')

print(din_guests)

message_0 = din_guests[0].title() + ", woud you like to go to dinner?"
message_1 = din_guests[1].title() + ", woud you like to go to dinner?"
message_2 = din_guests[2].title() + ", woud you like to go to dinner?"
message_3 = din_guests[3].title() + ", woud you like to go to dinner?"
message_4 = din_guests[4].title() + ", woud you like to go to dinner?"
message_5 = din_guests[5].title() + ", woud you like to go to dinner?"

print(message_0)
print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)

#remove all but two people from the list usng pop.  invite the remining two.  then delete the last two names from the list and print a blank list.
print(din_guests)

message = "I can now only invite two people to dinner.  DEATH MATCH!!!!\n"
print(message)

drop_guest = din_guests.pop(-1)

message = "Hello, " + drop_guest + "." + "\nYou are no longer invited to dinner because you're dumb."
print(message)
print(din_guests)

message = "Hello, " + drop_guest + "." + "\nYou are no longer invited to dinner because you're dumb."
print(message)
print(din_guests)

message = "Hello, " + drop_guest + "." + "\nYou are no longer invited to dinner because you're dumb."
print(message)
print(din_guests)

message = "Hello, " + drop_guest + "." + "\nYou are no longer invited to dinner because you're dumb."
print(message)
print(din_guests)


message_0 = "Hello, " + din_guests[0].title() + "!" + "\nYou still get to join me for dinner because you're NOT dumb."
message_1 = "Hello, " + din_guests[1].title() + "!" + "\nYou still get to join me for dinner because you're NOT dumb."
print(message_0)
print(message_1)

del din_guests[0]
del din_guests[1]

message = "There should be no one left on the list."
print(message)

print(din_guests)

