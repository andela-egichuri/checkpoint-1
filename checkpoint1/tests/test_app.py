import unittest
from checkpoint1.room import Room
from checkpoint1.user import User
import os

"""
	This class tests the methods implemented which are expected to return data
"""

 
class TestAppMethods(unittest.TestCase):

	#Setup the testing class
	def setUp(self):
		#Create an instance of the User and Room classes
		self.room_inst = Room()
		self.user_inst = User()
		
	""" Test that the rooms function returns a list of all room IDs given
	 the room type. (In this case O is passed for Offices) """
	def test_rooms_list(self):
		room_list = self.room_inst.rooms("O")
		self.assertIsInstance(room_list, list)

	#Test the function checking for available rooms
	def test_available_rooms(self):
		available_rooms = self.room_inst.available("O")
		self.assertIsInstance(available_rooms, list)

	#Test the function getRoom which returns the details of a given room
	def test_get_room(self):
		get_room = self.room_inst.getRoom("roo12")
		self.assertIsInstance(get_room, dict)

	#Test the function that returns the members of a given room
	def test_room_members(self):
		room_members = self.room_inst.members("uid", "L")
		self.assertIsInstance(room_members, list)

	def test_unallocated(self):
		unallocated_users = self.user_inst.unallocated("F")
		self.assertIsInstance(unallocated_users, dict)

	def test_user_list(self):
		fellow_list = self.user_inst.users("F")
		staff_list = self.user_inst.users("S")
		self.assertEqual(type(fellow_list), type(staff_list))

	def test_get_user(self):
		fellow_list = self.user_inst.users("F")
		get_user = self.user_inst.getUser(fellow_list[0])
		self.assertIn(get_user["userID"], fellow_list)

if __name__ == '__main__':
    unittest.main()
 
    