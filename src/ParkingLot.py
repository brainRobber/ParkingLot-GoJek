from constants import ErrorConstants as error

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
			print(error.INVALID_NUMBER_OF_SLOTS)
			return

		try:
			self.slots = [None for i in range(0, (self.max_size+1))]
			self.map_slot_to_cars = {}
			self.map_regno_to_slot = {}
			self.map_color_to_list_of_regno = {}

			print("created parking lot with %s spaces" % lot_space)
		except Exception as e:
			print(e)
		print("")

	def park(self, car_reg_no, car_color):
		if self.max_size == -1:
			print(error.PARKING_LOT_NOT_CREATED)
		elif len(self.map_slot_to_cars) == self.max_size:
			print(error.PARKING_LOT_FULL)
		else:
			car = Car(car_reg_no, car_color)
			for i in range(1, (self.max_size + 1)):
				if not self.slots[i]:
					self.slots[i] = car
					self.map_slot_to_cars[i] = car
					self.map_regno_to_slot[car_reg_no] = i
					if car_color in self.map_color_to_list_of_regno:
						self.map_color_to_list_of_regno[car_color].append(car_reg_no)
					else:
						self.map_color_to_list_of_regno[car_color] = []
						self.map_color_to_list_of_regno[car_color].append(car_reg_no)
					print("Allocated slot number: %s" % str(i))
					break
		print("")

	def leave(self, slot_no):
		if self.max_size == -1:
			print(error.PARKING_LOT_NOT_CREATED)
		elif len(self.map_slot_to_cars) > 0:
			car_to_leave = self.map_slot_to_cars.get(int(slot_no))
			if car_to_leave:
				try:
					self.slots[int(slot_no)] = None
					del self.map_slot_to_cars[int(slot_no)]
					del self.map_regno_to_slot[car_to_leave.reg_no]
					if car_to_leave.reg_no in self.map_color_to_list_of_regno.get(car_to_leave.color):
						self.map_color_to_list_of_regno[car_to_leave.color].remove(car_to_leave.reg_no)
						if self.map_color_to_list_of_regno[car_to_leave.color] == []:
							del self.map_color_to_list_of_regno[car_to_leave.color]
					print("Slot Number %s is Free." % slot_no)
				except Exception as e:
					print(e)
			else:
				print("Slot Number %s is already Empty" % slot_no)
		else:
			print(error.PARKING_LOT_EMPTY)
		print("")

	def status(self):
		if self.max_size == -1:
			print(error.PARKING_LOT_NOT_CREATED)
		elif len(self.map_slot_to_cars) > 0:
			print("Slot No\tRegistration No\tColor")
			for i in range(1, self.max_size+1):
				car = self.map_slot_to_cars.get(i)
				if car:
					print(str(i) + "\t" + car.reg_no + "\t" + car.color)
		else:
			print(error.PARKING_LOT_EMPTY)
		print("")

	def registration_numbers_for_cars_with_colour(self, color):
		if self.max_size == -1:
			print(error.PARKING_LOT_NOT_CREATED)
		elif color in self.map_color_to_list_of_regno:
			print(', '.join(self.map_color_to_list_of_regno[color]))
		else:
			print(error.NOT_FOUND)
		print("")

	def slot_numbers_for_cars_with_colour(self, color):
		if self.max_size == -1:
			print(error.PARKING_LOT_NOT_CREATED)
		elif color in self.map_color_to_list_of_regno:
			reg_no_list = self.map_color_to_list_of_regno[color]
			slot_list = []
			for i in range(len(reg_no_list)):
				slot_list.append(self.map_regno_to_slot[reg_no_list[i]])
			slot_list.sort()
			slot_list_str = [str(x) for x in slot_list]
			print(", ".join(slot_list_str))
		else:
			print(error.NOT_FOUND)
		print("")

	def slot_number_for_registration_number(self, reg_no):
		if self.max_size == -1:
			print(error.PARKING_LOT_NOT_CREATED)
		elif len(self.map_slot_to_cars) > 0:
			slot = self.map_regno_to_slot.get(reg_no)
			if slot:
				print(self.map_regno_to_slot[reg_no])
			else:
				print(error.NOT_FOUND)
		print("")