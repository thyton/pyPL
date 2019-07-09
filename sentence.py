"""
sentence.py
Defines sentence 
"""
import numpy as np
import copy 

class AtomicSentence:
	"""An atomic sentence consists of 
		- its symbol 
		- whether it is a positive literal
		- its true table
	For example: p is a positive literal -> positive == true
				 ¬p is a negative literal -> positive == false
	"""

	def __init__(self, positive = None, symbol = None):
		try:
			assert(isinstance(positive, bool))
			self._p = positive
		except:
			print("'positive' is not a bool type.")

		try:
			assert(symbol is not None and isinstance(symbol, str))
			self._s = symbol
			if self._s == "True":
				self._p = True
				self._t = np.array(True)
			elif self._s == "False":
				self._p = True
				self._t = np.array(False)
			else:
				self._t = np.array([True, False])
		except:
			print("No string symbol for the proposition is given")

	def table(self):
		return self._t

	def set(self, val):
		cp = copy.deepcopy(self)
		cp._t = np.array(val)
		return cp

	# magic	
	def __str__(self):
		# neg = bytes.decode(172)
		neg = "-"
		return self._s if self._p else neg + self._s

	def __not__(self):
		cp = Sentence(cp)
		cp = not cp
		return cp

	# fake method to test if an object is of AtomicSentence
	def atom(self):
		return 

import pyPL.connective

class Sentence(AtomicSentence):
	pass
	def __init__(self, obj):
		try:
			obj.atom()
			self._p = obj._p	# is positive
			self._s = obj._s   # symbol
			self._t = obj._t   # truth table

			try:
				obj.complex()
				self._pns = obj._pns	# a queue that represents postfix notation string of of the complex sentence
			except:
				self._pns = [obj._pns]
		except:
			print("Argument 'obj' is not an instance of AtomicSentence")
	
	# magic - some logical connectives


	# overriden __not__ from the base class
	def __not__():
		self = not self._p
		self._pns += Conn.NOT
		print(self._pns)

	# fake method to test if an objec is of Sentence
	def complex(self):
		return








