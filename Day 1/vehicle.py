class Vehicle():
	"""docstring for Vehicle"""
	def __init__(self, name, horsepower, cost, top_speed):
		self.name = name
		self.horsepower = horsepower
		self.cost = cost
		self.top_speed = top_speed

		self.engine_state = False
	
	def get_model(self):
		print(self.name)

	def accelerate(self):
		if self.engine_state is False:
			print("Engine is off. Turn engine on first...")
		else:
			print("Speeding up ...")

	def apply_brakes(self):
		if self.engine_state is True:
			print("Slowing down...")

	def turn_on_ignition(self):
		self.engine_state = True
		print("Engine is on.. Vroom vroom...")

	def turn_off_ignition(self):
		self.engine_state = False
		print("Engine is off")