class ParkingLot(object):
	class Car(object):
		def __init__(self, reg_no, color):
			self.reg_no = reg_no
			self.color = color

		def __str__(self):
			return "%s %s" % (self.reg_no, self.color)

	map_slot_to_cars = None
	map_regno_to_slot = None
	map_color_to_list_of_regno = None

	def __init__(self):
		self.max_size = -1
		self.slots = None

	def create_parking_lot(self, lot_space):
		try:
			self.max_size = int(lot_space)
		except ValueError:
			print("Invalid Lot Count")
			return

		try:
			self.slots = [None for i in range(0, (self.max_size+1))]
			self.map_slot_to_cars = {}
			self.map_regno_to_slot = {}
			self.map_color_to_list_of_regno = {}

			print("created parking lot with %s spaces" % lot_space)
		except Exception as e:
			print(e)

	def park(self, car_reg_no, car_color):
		pass

	def leave(self, slot_no):
		pass

	def status(self):
		pass

	def registration_numbers_for_cars_with_colour(self, color):
		pass

	def slot_numbers_for_cars_with_colour(self, color):
		pass

	def slot_number_for_registration_number(self, reg_no):
		pass