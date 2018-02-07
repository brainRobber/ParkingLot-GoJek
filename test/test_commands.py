import unittest
from src.commands import Command

class CommandsTest(unittest.TestCase):
	def setUp(self):
		self.commands = Command()

	def test(self):
		self.assertEqual(len(self.commands.commandMap) == 0, False)
		self.assertEqual("create_parking_lot" in self.commands.commandMap, True)
		self.assertEqual("park" in self.commands.commandMap, True)
		self.assertEqual("leave" in self.commands.commandMap, True)
		self.assertEqual("status" in self.commands.commandMap, True)
		self.assertEqual("registration_numbers_for_cars_with_colour" in self.commands.commandMap, True)
		self.assertEqual("my_test_command" in self.commands.commandMap, False)


if __name__ == '__main__':
    unittest.main()