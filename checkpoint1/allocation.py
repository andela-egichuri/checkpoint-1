import room, random, user

class Allocation(object):


	def __init__(self):
		pass

	def allocate(self, room_type, member):
		#Check if there are available rooms
		space = room.Room()
		available_rooms = space.available(room_type)
		if len(available_rooms) <= 0:
			if room_type == "O":
				print "Sorry, there are no more available office spaces"
			elif room_type == "L":
				print "Sorry, there are no more available living spaces"
		else:
			rand_room = random.choice(available_rooms)
			space.addMember(rand_room, room_type, member)


	def allocateAll(self, user_type):
		#Get unallocated users
		users = user.User()
		to_allocate = users.unallocated(user_type)

		#Allocate office spaces
		for member in to_allocate["office"]:
			self.allocate("O", member)

		#Allocate living spaces only to fellows
		if user_type == "F":
			for member in to_allocate["living"]:
				user_details =  users.getUser(member)
				if user_details["accomodation"] == "Y":
					self.allocate("L", member)

