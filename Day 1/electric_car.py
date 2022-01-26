import car

class electric_car(car.Car):
	"""docstring for electric_car"""
	def __init__(self, name, horsepower, cost, top_speed, battery_capacity):
		super().__init__(name, horsepower, cost, top_speed)
		self.battery_capacity = battery_capacity

	def charge_battery(self):
		print('Charge battery')



if __name__ == '__main__':
	x = electric_car('Tesla', 800, 280000, 300, 1000)
	x.turn_on_ignition()
	x.turn_off_ignition()
	x.open_door()
	x.charge_battery()