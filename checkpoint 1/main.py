import user, room, json, allocation, functions


source = raw_input("Enter 1 to add user data manually or 2 to select an existing file:\n")


while source != "1" and source != "2":
		source = raw_input("Try again. Enter 1 to add user data manually or 2 to select an existing file: \n").lower()


if source == "1":
	functions.addUser()
elif source == "2":
	functions.readInput('rooms.txt', "rooms")
'''

source = raw_input("Enter 1 to add user data manually or 2 to select an existing file:\n")


while source != "1" and source != "2":
		source = raw_input("Try again. Enter 1 to add user data manually or 2 to select an existing file: \n").lower()


if source == "1":
	newuser = user.User()
	newuser.addUser()
elif source == "2":
	functions.readInput('input.txt', "users")


user_type = raw_input("User Type? Enter S for staff and F for fellow: \n").upper()

while user_type != "F" and user_type != "S":
	user_type = raw_input("Try again. Enter S for staff and F for fellow: \n").upper()



print functions.listUsers(user_type)
'''