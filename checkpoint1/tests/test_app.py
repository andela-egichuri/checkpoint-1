import unittest
from checkpoint1.room import Room
from checkpoint1.user import User
import os
import json
import random


class TestAppMethods(unittest.TestCase):

    """
    This class tests the methods implemented which are expected to return data
    """

    def setUp(self):
        '''
        Setup the testing class
        '''
        # Create an instance of the User and Room classes
        self.room_inst = Room(os.path.dirname(os.path.abspath(__file__)))
        self.test_users = User(os.path.dirname(os.path.abspath(__file__)))
        d_path = os.path.dirname(os.path.abspath(__file__))
        user_data = os.path.join(d_path, "data/users.json")
        room_data = os.path.join(d_path, "data/rooms.json")
        alloc_data = os.path.join(d_path, "data/Allocations.txt")

        with open(user_data, 'w+') as file:
            # Initialize test user data into data files
            data = {
                "users": {
                    "fellows": {
                        "tes23": {
                            "accomodation": "Y",
                            "username": "Test User"
                        }
                    },
                    "staff": {
                        "tes24": {
                            "accomodation": "N/A",
                            "username": "Test Staff"
                        }
                    }
                }
            }
            file.write(json.dumps(data, indent=4, sort_keys=True))

        with open(room_data, "w+") as file:
            # Initialize test room data into data files
            data = {
                "rooms": {
                    "living": {
                        "roo12": {
                            "name": "Room Test"
                        }
                    },
                    "office": {
                        "off13": {
                            "name": "office Test"
                        }
                    }
                }
            }
            file.write(json.dumps(data, indent=4, sort_keys=True))

        with open(alloc_data, 'w+') as file:
            pass

    """ Test that the rooms function returns a list of all room IDs given
	 the room type. (In this case O is passed for Offices) """

    def test_rooms_list(self):
        print os.path.dirname(os.path.abspath(__file__))
        room_list = self.room_inst.rooms("O")
        self.assertIsInstance(room_list, list)

    # Test the function checking for available rooms
    def test_available_rooms(self):
        available_rooms = self.room_inst.available("O")
        self.assertIsInstance(available_rooms, list)

    # Test the function getRoom which returns the details of a given room
    def test_get_room(self):
        get_room = self.room_inst.getRoom("roo12")
        self.assertIsInstance(get_room, dict)

    # Test the function that returns the members of a given room
    def test_room_members(self):
        room_members = self.room_inst.members("tes23", "L")
        self.assertIsInstance(room_members, list)

    def test_unallocated(self):
        unallocated_users = self.test_users.unallocated("F")
        self.assertIsInstance(unallocated_users, dict)

    def test_save_user(self):
        self.test_users.user_type = "F"
        self.test_users.user_name = "User Testing"
        self.test_users.accomodation = "Y"
        self.test_users.user_id = "use12"
        self.test_users.saveUser()

    def test_user_list(self):
        fellow_list = self.test_users.users("F")
        staff_list = self.test_users.users("S")
        self.assertEqual(type(fellow_list), type(staff_list))

    def test_get_user(self):
        fellow_list = self.test_users.users("F")
        get_user = self.test_users.getUser(fellow_list[0])
        self.assertIn(get_user["userID"], fellow_list)


if __name__ == '__main__':
    unittest.main()
