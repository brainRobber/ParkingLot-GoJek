from command import Command
from parking_lot import ParkingLot
from constants import ErrorConstants as error

class InputParser(object):
	def __init__(self):
		self.comands = Command()
		self.parking_lot = ParkingLot()

	def parse_text_input(self, inputString):
		inputs = inputString.split(" ")
		if len(inputs) == 1:
			method = self.comands.commandsMap.get(inputString)
			if method is not None:
				try:
					method(self.parking_lot)
				except Exception as e:
					print(e)
			else:
				print(error.INVALID_INPUT)

		elif len(inputs) == 2:
			method = self.comands.commandsMap.get(inputs[0])
			if method is not None:
				try:
					method(self.parking_lot, inputs[1])
				except Exception as e:
					print(e)
			else:
				print(error.INVALID_INPUT)

		elif len(inputs) == 3:
			method = self.comands.commandsMap.get(inputs[0])
			if method is not None:
				try:
					method(self.parking_lot, inputs[1], inputs[2])
				except Exception as e:
					print(e)
			else:
				print(error.INVALID_INPUT)
		else:
			print("Incorrect number of arguments: (1, 2, 3 expected)")

	def parse_file_input(self, filepath):
		pass