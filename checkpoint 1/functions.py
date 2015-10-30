import user, room, json, random




def readInput(filename, src):
	with open(filename, 'r') as f:		
		if src == "rooms":
			for line in f:
				words = line.split("\t")		    
				room_type = words[1].upper().strip()
				name = words[0].upper().strip()			   
				newroom = room.Room(room_type, name)
				newroom.saveRoom()

		elif src == "users":
			for line in f:
				newuser = user.User()
				words = line.split("\t")	
				print "save " 
				print words
				print "\n"	    
				newuser.user_type = words[1].upper().strip()
				newuser.user_name = words[0].upper().strip()
				newuser.accomodation = words[2].upper().strip()	
				newuser.user_id = newuser.user_name[0:3].lower() + str((random.randint(10,100)))	    
				newuser.saveUser()



