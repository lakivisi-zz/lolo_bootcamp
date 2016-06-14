class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name

	def call(self):
		print ("hello",self.name)
		
loice = Person("loice")
print loice.call()