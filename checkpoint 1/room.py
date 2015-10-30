import random, json 

class Room(object):
	def __init__(self, room_type, room_name):
		self.room_type = room_type
		self.name = room_name
		self.occupants = []
		self.room_id = room_name[0:3].lower() + str((random.randint(10,100)))

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

	def members(self, room):
		pass




	

