import user, room, json, random, os, allocation
selection = ""

def readInput(filename, src):
	try:
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
	except IOError as e:
		print "File not found"


def home():
	os.system('clear')
	print "MENU OPTIONS"
	print "********************************************************************"

	print "Select an option below to continue"
	selection = raw_input("1: Add users \n2: Add rooms \n3: View all allocations \n4: View allocations per room \
	 \n5: View all users in the system \n6: View users pending space allocation \
	 \n7: Allocate living and office space to users\n8: View available rooms\n9: Exit\n:")
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
		user_type = raw_input("Try again.\n S: Staff \n F: Fellow \n C: Cancel \n:").upper()

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
	try:
		selection
	except NameError:
		selection = ""
	while selection != "x":
		# Add users
		if selection == "1":
			addUsers()

		# Add rooms
		elif selection == "2":
			addRooms()

		# View all allocations
		elif selection == "3":
			print "\n"
			room_inst = room.Room()
			roomlist = room_inst.rooms("O")
			roomlist = roomlist + room_inst.rooms("L")
			for roomid in roomlist:
				userlist = ""
				users = user.User()
				room_details = room_inst.getRoom(roomid)
				room_members = room_details["occupants"]
				if len(room_details["occupants"]) > 0:
					print room_details["name"]
				for member in room_members:
					user_details =  users.getUser(member)
					userlist = userlist + user_details["username"] + ", "
				if len(room_details["occupants"]) > 0:
					print userlist + "\n"
			action = raw_input("\n1: Continue \n:")
			while action != "1":
				action = raw_input("\n1: Continue \n:")
			if action == "1":
				menu()

		# Print members per room
		elif selection == "4":
			print "\n"
			os.system('clear')
			room_type = raw_input("Enter Room Type: \n 1: Office space \n 2: Living space \n:")

			while room_type != "1" and room_type != "2":
				room_type = raw_input("Try again. Enter Room Type:\n 1: Office space \n 2: Living space \n:")
			if room_type == "1":
				rtype = "O"
			elif room_type == "2":
				rtype = "L"
			print "\n"
			print "Select one room from the list below"
			room_inst = room.Room()
			roomlist = room_inst.rooms(rtype)
			for each in roomlist:
				theroom = room_inst.getRoom(each)
				print " " + theroom["name"] + "\t(Room ID: " + theroom["roomID"] + ")"
			selected = raw_input("\nEnter Room ID \n:").lower()
			for roomid in roomlist:
				users = user.User()
				if roomid == selected:
					room_details = room_inst.getRoom(selected)
					room_members = room_details["occupants"]
					for member in room_members:
						user_details =  users.getUser(member)
						print user_details["username"]
			action = raw_input("\n1: Continue \n:")
			while action != "1":
				action = raw_input("\n1: Continue \n:")
			if action == "1":
				menu()

		# Print users
		elif selection == "5":
			showUsers()

		# View unallocated users
		elif selection == "6":
			user_type = raw_input("\n S: Staff \n F: Fellow \n C: Cancel \n:").upper()
			while user_type != "F" and user_type != "S" and user_type != "C":
				user_type = raw_input("Try again.\nS: Staff \nF: Fellow \n C: Cancel \n:").upper()

			if user_type == "C":
				menu()
			else:
				users = user.User()
				users.view_unallocated(user_type)
			action = raw_input("\n1: Continue \n:")
			while action != "1":
				action = raw_input("\n1: Continue \n:")
			if action == "1":
				menu()

		# Allocate rooms
		elif selection == "7":
			user_type = raw_input("\n S: Staff \n F: Fellow \n C: Cancel \n:").upper()
			while user_type != "F" and user_type != "S" and user_type != "C":
				user_type = raw_input("Try again.\nS: Staff \nF: Fellow \n C: Cancel \n:").upper()

			if user_type == "C":
				menu()
			else:
				allocate = allocation.Allocation()
				allocate.allocateAll(user_type)
			action = raw_input("\n1: Continue \n:")
			while action != "1":
				action = raw_input("\n1: Continue \n:")
			if action == "1":
				menu()

		elif selection == "8":
			space = room.Room()
			print "\n"
			print "AVAILABLE OFFICE SPACES"
			print "*****************************************************"
			availableOffices = space.available("O")
			for each in availableOffices:
				details = space.getRoom(each)
				av = 6 - len(details["occupants"])
				print details["name"] + ": " + str(av) + " Spaces"
			print "\n"
			print "AVAILABLE LIVING SPACES"
			print "*****************************************************"
			availableLiving = space.available("L")
			for each in availableLiving:
				details = space.getRoom(each)
				av = 4 - len(details["occupants"])
				print details["name"] + ": " + str(av) + " Spaces"
			action = raw_input("\n1: Continue \n:")
			while action != "1":
				action = raw_input("\n1: Continue \n:")
			if action == "1":
				menu()

		elif selection == "9":
			selection = "x"

		else:
			selection = home()

menu()
