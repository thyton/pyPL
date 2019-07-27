"""
sentence.py
Defines sentence 
"""
import numpy as np
import copy
import sys
from .literal import *
from .exp_tree import * 

class AtomicSentence:
	"""An atomic sentence consists of 
		- its symbol 
		- whether it is a positive literal
		- its true table
	For example: p is a positive literal -> positive == true
				 ¬p is a negative literal -> positive == false
	"""

	def __init__(self, positive = None, symbol = None):
		self.l = Literal(positive, symbol)
		if self.l.equalSymbol("True") or self.l.equalSymbol("False"):
			self.t = np.array(True)
		else:
			self.t = np.array([True, False])

	def table(self):
		return self.t

	def set(self, val):
		cp = copy.deepcopy(self)
		cp.t = np.array(val)
		return cp

	def setSymbol(self, symbol):
		self.l.setSymbol(symbol)

	# logical connectives
	def cAnd (self, other):
		cpSelf = Sentence(self)
		cpOther = Sentence(copy.deepcopy(other))
		cpSelf.cAnd(cpOther)
		return cpSelf

	def cOr (self, other):
		cpSelf = Sentence(self)
		cpOther = Sentence(copy.deepcopy(other))
		cpSelf.cOr(cpOther)
		return cpSelf

	def cImp(self, other):
		cpSelf = Sentence(self)
		cpOther = Sentence(copy.deepcopy(other))
		cpSelf.cImp(cpOther)
		return cpSelf

	def cIff(self, other):
		cpSelf = Sentence(self)
		cpOther = Sentence(copy.deepcopy(other))
		cpSelf.cIff(cpOther)
		return cpSelf		

	def cnf(self):
		cpSelf = Sentence(self)
		return cpSelf.cnf()
		
	# fake method to test if an object is of AtomicSentence
	def atom(self):
		return 

	# magic	
	def __str__(self):
		# neg = bytes.decode(172)
		return str(self.l)

	def __invert__(self):
		cp = Sentence(self)
		cp = ~cp
		return cp

from pyPL.connective import *
class Sentence:
	def __init__(self, obj):
		try:
			self.l = obj.l
			if isinstance(obj, Sentence):
				self.pns = obj.pns	# a queue that represents postfix notation string of of the complex sentence
			else:
				self.pns = []
				self.pns.append(self.l)
		except AttributeError as e:
			print("'obj' is not an instance of Sentence")
	

	# logical connectives
	def cAnd (self, other):
		cpOther = other
		if not isinstance(other, Sentence):
			cpOther = Sentence(copy.deepcopy(other))
		self.pns.extend(cpOther.pns)
		self.pns.append(Conn.AND)
		return self

	def cOr (self, other):
		cpOther = other
		if not isinstance(other, Sentence):
			cpOther = Sentence(copy.deepcopy(other))
		self.pns.extend(cpOther.pns)
		self.pns.append(Conn.OR)
		return self

	def cImp(self, other):
		cpOther = other
		if not isinstance(other, Sentence):
			cpOther = Sentence(copy.deepcopy(other))
		self.pns.extend(cpOther.pns)
		self.pns.append(Conn.IMP)
		return self

	def cIff(self, other):	
		cpOther = other
		if not isinstance(other, Sentence):
			cpOther = Sentence(copy.deepcopy(other))
		self.pns.extend(cpOther.pns)
		self.pns.append(Conn.IFF)
		return self

	# magic - some logical connectives
	def __str__(self):
		# include the literal ? 
		# but needs to manually enter the literal
		# that doesnt conflict with the current literals
		s = [str(e) for e in self.pns]
		return str(s)

	# operator NOT
	def __invert__(self):
		self.pns.append(Conn.NOT)
		return self

	def cnf(self):
		et = ExpTree(self.pns)
		return et.cnf()





