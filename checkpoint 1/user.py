import json
import random

class User(object):
	def __init__(self):
		self.user_type = ""
		self.user_name = ""
		self.accomodation = ""
		self.user_id = ""
		

	def saveUser(self):
		tosave = {"username" : self.user_name,  "accomodation" : self.accomodation}
				
		with open("users.json", "r+") as data_file:
			data = json.load(data_file)
			if self.user_type == "F":
				data["users"]["fellows"][self.user_id] = tosave
			elif self.user_type == "S":
				data["users"]["staff"][self.user_id] = tosave
			data_file.seek(0)  # rewind to beginning of file
			data_file.write(json.dumps(data, indent=4, sort_keys=True))
 

	def addUser(self):		
		user_type = raw_input("User Type? Enter S for staff and F for fellow: \n").upper()

		while user_type != "F" and user_type != "S":
			user_type = raw_input("Try again. Enter S for staff and F for fellow: \n").upper()

		name = raw_input("Enter name: \n").upper()

		if user_type == "F":
			accomodation = raw_input("Does the fellow need living space? (Y or N): \n").upper()
			while accomodation != "Y" and accomodation != "N":
				accomodation = raw_input("Try again. Allocate living space? (Y or N): \n").upper()

		elif user_type == "S":
			accomodation = "N/A"

		self.user_type = user_type
		self.user_name = name  
		self.accomodation = accomodation
		self.user_id = self.user_name[0:3].lower() + str((random.randint(10,100)))

		self.saveUser() 


	def printUsers(self, user_type):
		pass

	def unallocated(self):
		userlist = ""
		with open('users.json', 'r') as f:
			data = json.load(f)
			if user_type == "F":
				users = data["users"]["fellows"]
			elif user_type == "S":
				users = data["users"]["staff"]

			for key in users:
				print users[key]
				'''if alloc_key not in users[key]:
					userlist = userlist + key + "\t" + user_type + "\t"
					for each, value in users[key].iteritems():
						userlist = userlist + value + "\t" '''

				#userlist = userlist + "\n"
		return userlist


	def listUsers(self, user_type):
		userlist = ""
		with open('users.json', 'r') as f:
			data = json.load(f)
			if user_type == "F":
				users = data["users"]["fellows"]
			elif user_type == "S":
				users = data["users"]["staff"]

		for key in users:
			#print users[key]
			userlist = userlist + key + "\t" + user_type + "\t"
			for each, value in users[key].iteritems():
				userlist = userlist + value + "\t"

			userlist = userlist + "\n"
		return userlist

#print listUsers()
print unallocated()