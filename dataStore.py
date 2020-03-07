class DataStore:
	__instance = None
	roll = 0.0
	orientation = 0

	@staticmethod
	def getInstance():
		""" Static access method. """
		if DataStore.__instance == None:
			DataStore()
		return DataStore.__instance

	def __init__(self):
		if DataStore.__instance is not None:
			raise Exception("singleton bruh")
		else:
			DataStore.__instance = self
	def setRoll(self, r):
		self.roll = r

	def getRoll(self):
		return self.roll

	def setOrientation(self, ori):
		self.orientation = ori

	def getOrientation(self):
		return self.orientation
