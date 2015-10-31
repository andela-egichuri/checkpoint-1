import random, json 

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
			if self.room_type == "L":
				data["rooms"]["living"][self.room_id] = tosave
			elif self.room_type == "O":
				data["rooms"]["offices"][self.room_id] = tosave
			data_file.seek(0)  # rewind to beginning of file
			data_file.write(json.dumps(data, indent=4, sort_keys=True))


	def members(self, room_id, room_type):
		memberlist = []
		if room_type == "O":
			rtype = "offices"
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
				rooms = data["rooms"]["offices"]
			elif room_type == "L":
				rooms = data["rooms"]["living"]

		for key in rooms:
			#print key		
			roomlist.append(key)

		return roomlist



	def available(self, room_type):
		#occupied = room.Room()
		roomlist = []
		rooms = self.rooms(room_type)
		for eachroom in rooms:
			occupants = self.members(eachroom, room_type)
			if room_type == "O":
				if len(occupants) < 4:
					roomlist.append(eachroom)
			elif room_type == "L":
				if len(occupants) < 4:
					roomlist.append(eachroom)
		return roomlist


	def addMember(self, room_id, room_type, member):
		print room_id, room_type, member

		with open("rooms.json", "r+") as data_file:
			data = json.load(data_file)
			if room_type == "L":
				data["rooms"]["living"][room_id]["occupants"].append(member)
			elif room_type == "O":
				data["rooms"]["offices"][room_id]["occupants"].append(member)
			data_file.seek(0)  # rewind to beginning of file
			data_file.write(json.dumps(data, indent=4, sort_keys=True))