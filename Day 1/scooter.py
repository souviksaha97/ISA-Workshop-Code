import vehicle

class Scooter(vehicle.Vehicle):
	"""docstring for Scooter"""
	def __init__(self, name, horsepower, cost, top_speed):
		super().__init__(name, horsepower, cost, top_speed)

	def apply_stand(self):
		print('Stand on')

	def drop_stand(self):
		print('Stand off')


if __name__ == '__main__':
	x = Scooter('Scootey', 80, 5, 90)
	x.apply_stand()
	x.drop_stand()