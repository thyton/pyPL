import copy

class Literal:
	"""An literal consists of 
		- its symbol 
		- whether it is a positive literal
	   "True" and "False" are positive literals	
	"""
	def __init__(self, positive = None, symbol = None):
		try:
			assert(isinstance(positive, bool))
			self.p = positive
		except:
			print("'positive' is not a bool type.")

		try:
			assert(symbol is not None and isinstance(symbol, str))
			self.s = symbol
			if self.s == "True" or self.s == "False":
				self.p = True
		except:
			print("No string symbol for the proposition is given")\

	def isPositive(self):
		return self.p

	def isNegative(self):
		return not self.p

	def complements(self, other):
		return self.s == other.s and self.p != self.p

	def equalSymbol(self, other):
		return self.s == other.s

	def equalSymbol(self, symbol):
		return self.s == symbol

	def setSymbol(self, symbol):
		self.s = symbol

	# fake function to test if an object is of Literal
	def literal():
		return

	# overridden
	def __deepcopy__(self, memo):
		cp = Literal(copy.deepcopy(self.p, memo), copy.deepcopy(self.s, memo))
		return cp

	def __copy__(self):
		return copy.copy(self)

	# magic
	def __invert__(self): # perhaps make it a deep copy?
		# cp = copy.deepcopy(self)
		# cp.p = not self.p
		# return cp
		self.p = not self.p
		return self

	def __eq__(self, other):
		return self.s == other.s and self.p == self.p

	def __hash__(self):
		return hash((self.s, self.p))
				
	def __ne__(self, other):
		return self.s != other.s or self.p == self.p

	def __str__(self):
		neg = "-"
		return self.s if self.p else neg + self.s

	def __iter__(self):
		return self

