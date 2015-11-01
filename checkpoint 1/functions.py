import user, room, json, random, os
selection = ""
def readInput(filename, src):
	with open(filename, 'r') as f:
		if src == "rooms":
			for line in f:
				newroom = room.Room()
				words = line.split("\t")
				newroom.room_type = words[1].upper().strip()
				newroom.name = words[0].upper().strip()
				newroom.room_id = newroom.name[0:3].lower() + str((random.randint(10,100)))
				newroom.saveRoom()

		elif src == "users":
			for line in f:
				newuser = user.User()
				words = line.split("\t")
				newuser.user_type = words[1].upper().strip()
				newuser.user_name = words[0].upper().strip()
				newuser.accomodation = words[2].upper().strip()
				newuser.user_id = newuser.user_name[0:3].lower() + str((random.randint(10,100)))
				newuser.saveUser()


def home():
	os.system('clear')
	print "MENU OPTIONS"
	print "********************************************************************"

	print "Select an option below to continue"
	selection = raw_input("1: Add users \n2: Add rooms \n3: View all users in the system \n4: View pending space allocation\n:")
	return selection


def addUsers():
	print "\n"
	print "ADD USERS"
	print "********************************************************************"
	source = raw_input("1: Add user data manually \n2: to select an existing file \n3: Cancel\n:")


	while source != "1" and source != "2" and source != "3":
		source = raw_input("Try again.\n1: Add user data manually \n2: to select an existing file: \n3: Cancel\n:")


	if source == "1":
		newuser = user.User()
		newuser.addUser()
	elif source == "2":
		data_file = raw_input("Enter file name (including the file extension)\n")
		readInput(data_file, "users")
	elif source == "3":
		menu()

def addRooms():
	print "\n"
	print "ADD ROOMS"
	print "********************************************************************"
	source = raw_input("1: to add user data manually \n2: to select an existing file\n3: Cancel\n:")

	while source != "1" and source != "2" and source != "3":
		source = raw_input("Try again.\n1: to add user data manually \n2: to select an existing file:\n3: Cancel\n:")

	if source == "1":
		newroom = room.Room()
		newroom.addRoom()
	elif source == "2":
		data_file = raw_input("Enter file name (including the file extension)\n")
		readInput(data_file, "rooms")
	elif source == "3":
		menu()


def showUsers():
	users = user.User()
	print "View USERS"
	print "********************************************************************"
	user_type = raw_input("Select User Type\n S: Staff \n F: Fellow \n C: Cancel \n:").upper()

	while user_type != "F" and user_type != "S" and user_type != "C":
		user_type = raw_input("Try again.\nS: Staff \nF: Fellow \n C: Cancel \n:").upper()

	if user_type == "C":
		menu()
	else:
		print users.listUsers(user_type)
	action = raw_input("\n1: Continue \n:")
	while action != "1":
		action = raw_input("\n1: Continue \n:")
	if action == "1":
		menu()


def menu():
	selection = ""
	while selection != "x":

		# Add users
		if selection == "1":
			addUsers()

		# Add rooms
		elif selection == "2":
			addRooms()

		# Print users
		elif selection == "3":
			showUsers()

		# Allocate rooms

		# Print allocations

		# View unallocated users

		else:
			selection = home()
