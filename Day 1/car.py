import vehicle

class Car(vehicle.Vehicle):
	"""Class definition for a Car"""
	def __init__(self, name, horsepower, cost, top_speed):
		super().__init__(name, horsepower, cost, top_speed)
		
	def open_door(self):
		print('Open door')

	def close_door(self):
		print('Close door')


if __name__ == '__main__':
	x = Car('Swift', 800, 10, 180)
	x.open_door()
	x.turn_on_ignition()

