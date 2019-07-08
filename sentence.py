"""
sentence.py
Defines sentence 
"""
import numpy as np
import copy 

class AtomicSentence:
	" ""A truth table of a proposition"" "

	def __init__(self, val = None):	
		try:
			val
			self.v = val
		except:
			self.v = True

		self.t = np.array([True, False])

	def table(self):
		return self.t

	def set(self, val):
		return AtomicSentence(val)

	def val(self):
		return self.v


# class Sentence:
# 	pass
