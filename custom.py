class CustomClass(object):
	"""
	My custom class

	:param x: x variable
	:type x: int

	:param y: y variable
	:type y: int
	"""
	def __init__(self,x=1,y=2):
		self.x = x
		self.y = x

	def add(self):
		""" Adds two numbers

		:return: Sum of two numbers
		:rtype: float
		"""
		return self.x+self.y

def utility(s):
	"""
	A utility function that returns a string reversed

	:param s: The string to reverse
	:type s: str
	"""
	return s[::-1]

def newfunction(x):
	"""
	A new function that should appear in the automatically
	built documentation

	:param x: A test parameter
	:type x: int
	"""
	return x
