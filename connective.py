from enum import Enum
class Conn(Enum):
	"""An Enumeration for logical connectives in propositional logic"""
	NOT = 1
	AND = 2
	OR =  3
	IMP = 4 # implies
	IFF = 5

	def __str__(self):
		# s = {1:"¬", 2:'∧', 3:"∨", 4:"⇒", 5:"⇔"}
		s = {1:'not', 2:'and', 3:"or", 4:"imp", 5:"iff"}
		return s[self.value]