from enum import Enum

class Conn(Enum):
	"""An Enumeration for logical connectives in propositional logic"""
	NOT = 1
	AND = 2
	OR =  3
	IMP = 4 # implies
	IFF = 5
