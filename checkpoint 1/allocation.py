import room, random, user

class Allocation(object):


	def __init__(self):
		pass

	def allocate(self, room_type, member):
		#Check if there are available rooms
		space = room.Room()
		availableRooms = space.available(room_type)
		if len(availableRooms) <= 0:
			print "Sorry, there are no more available rooms"
		else:
			rand_room = random.choice(availableRooms)
			space.addMember(rand_room, room_type, member)
		print len(availableRooms)


	def allocateAll(self, user_type):
		#Get unallocated users
		users = user.User()
		toallocate = users.unallocated(user_type)

		#Allocate office spaces
		for member in toallocate["office"]:
			self.allocate("O", member)

		if user_type == "F":
			#Allocate living spaces
			for member in toallocate["living"]:
				if :
					pass
					pass
				pass

		#print toallocate


newallocation = Allocation()
newallocation.allocateAll("S")
print "\n"
newallocation.allocateAll("F")
