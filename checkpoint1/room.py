import random, json, user

class Room(object):
	def __init__(self):
		self.room_type = ""
		self.name = ""
		self.occupants = []
		self.room_id = ""


	def saveRoom(self):
		tosave = {"name" : self.name,  "occupants" : self.occupants}

		with open("rooms.json", "r+") as data_file:
			data = json.load(data_file)
			room_inst = Room()
			room_names = []
			if self.room_type == "L":
				room_list =  room_inst.rooms("L")
				for each_room in room_list:
					room_details = room_inst.getRoom(each_room)
					room_names.append(room_details["name"])
				if self.name not in room_names:
					data["rooms"]["living"][self.room_id] = tosave
					print "Room " + self.name +" added to the system"
				else:
					print "The room " + self.name +" is currently in the system"
			elif self.room_type == "O":
				room_list =  room_inst.rooms("O")
				for each_room in room_list:
					room_details = room_inst.getRoom(each_room)
					room_names.append(room_details["name"])
				if self.name not in room_names:
					data["rooms"]["office"][self.room_id] = tosave
					print "Room " + self.name +" added to the system"
				else:
					print "The room " + self.name +" is currently in the system"
			data_file.seek(0)  # rewind to beginning of file
			data_file.write(json.dumps(data, indent=4, sort_keys=True))

	def addRoom(self):
		room_type = raw_input("Enter Room Type: \n 1: Office space \n 2: Living space: \n")

		while room_type != "1" and room_type != "2":
			room_type = raw_input("Try again. Enter Room Type:\n 1: Office space \n 2: Living space: \n")

		if room_type == "1":
			rtype = "O"
		elif room_type == "2":
			rtype = "L"
		name = raw_input("Enter room name: \n").upper()
		self.room_type = rtype
		self.name = name
		self.room_id = self.name[0:3].lower() + str((random.randint(10,100)))
		self.saveRoom()

	def members(self, room_id, room_type):
		memberlist = []
		if room_type == "O":
			rtype = "office"
		elif room_type == "L":
			rtype = "living"
		with open('rooms.json', 'r') as f:
			data = json.load(f)
			rooms = data["rooms"][rtype]


		for keys in rooms:
			if keys == room_id:
				for key, value in rooms[keys].iteritems():
					#print each, value
					if key == "occupants":
						memberlist = value
		return memberlist


	def rooms(self, room_type):
		roomlist = []
		with open('rooms.json', 'r') as f:
			data = json.load(f)
			if room_type == "O":
				room = data["rooms"]["office"]
			elif room_type == "L":
				room = data["rooms"]["living"]

		for key in room:
			roomlist.append(key)

		return roomlist



	def available(self, room_type):
		#occupied = room.Room()
		roomlist = []
		rooms = self.rooms(room_type)
		for eachroom in rooms:
			occupants = self.members(eachroom, room_type)
			if room_type == "O":
				if len(occupants) < 6:
					roomlist.append(eachroom)
			elif room_type == "L":
				if len(occupants) < 4:
					roomlist.append(eachroom)
		return roomlist


	def addMember(self, room_id, room_type, member):
		#print room_id, room_type, member
		user_type = ""

		if room_type == "L":
			rtype = "living"
		elif room_type == "O":
			rtype = "office"

		with open("rooms.json", "r+") as data_file:
			data = json.load(data_file)
			data["rooms"][rtype][room_id]["occupants"].append(member)
			data_file.seek(0)  # rewind to beginning of file
			data_file.write(json.dumps(data, indent=4, sort_keys=True))

		with open("users.json", "r+") as data_file:
			data = json.load(data_file)
			if member in data["users"]["staff"]:
				data["users"]["staff"][member][rtype] = room_id
				user_type = "S"
			elif member in data["users"]["fellows"]:
				data["users"]["fellows"][member][rtype] = room_id
				user_type = "F"
			data_file.seek(0)  # rewind to beginning of file
			data_file.write(json.dumps(data, indent=4, sort_keys=True))

		users = user.User()
		user_details =  users.getUser(member)

		print "User " + user_details["username"] + " added to room " + room_id


	def getRoom(self, room_id):
		room_details = {}
		with open('rooms.json', 'r') as f:
			data = json.load(f)
			rooms = data["rooms"]["living"]
			rooms1 = data["rooms"]["office"]
		if room_id in rooms:
			room_details["roomID"] = room_id
			room_details["room_type"] = "LIVING"
			for each, value in rooms[room_id].iteritems():
				room_details[each] = value
		if room_id in rooms1:
			room_details["roomID"] = room_id
			room_details["room_type"] = "LIVING"
			for each, value in rooms1[room_id].iteritems():
				room_details[each] = value
		return room_details


