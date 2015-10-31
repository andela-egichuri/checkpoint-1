import room, random 

class Allocation(object):
	

	def __init__(self):
		pass

	def allocate(self, room_type, member):
		#Check if there are available rooms
		space = room.Room()
		availableRooms = space.available(room_type)
		rand_room = random.choice(availableRooms)
		space.addMember(rand_room, room_type, member)


	def save(self):
		pass


newallocation = Allocation()
newallocation.allocate("O")