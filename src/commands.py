from parking_lot import ParkingLot

class Command(object):
	def _populate_command_hash_map(self):
		self.commandsMap["create_parking_lot"] = ParkingLot.create_parking_lot
		self.commandsMap["park"] = ParkingLot.park
		self.commandsMap["leave"] = ParkingLot.leave
		self.commandsMap["status"] = ParkingLot.status
		self.commandsMap["registration_numbers_for_cars_with_colour"] = ParkingLot.registration_numbers_for_cars_with_colour
		self.commandsMap["slot_numbers_for_cars_with_colour"] = ParkingLot.slot_numbers_for_cars_with_colour
		self.commandsMap["slot_number_for_registration_number"] = ParkingLot.slot_number_for_registration_numbe

	def __init__(self):
		self.commandsMap = {}
		try:
			self._populate_command_hash_map()
		except Exception as e:
			print(e)

	def __str__(self):
		return self.commandsMap