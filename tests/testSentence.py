import sys
sys.path.append('../../')

from pyPL.sentence import AtomicSentence
import unittest
import numpy as np 

class testAtomicSentence(unittest.TestCase):
	def test_table(self):
		print(AtomicSentence(True, "p").table())

	def test_set(self):
		print(AtomicSentence(True, "True").set(False).table())

	def test_str(self):
		print(AtomicSentence(False, "p"))
		print(AtomicSentence(True, "p"))

	def test_neg(self):
		s = AtomicSentence(True, "p")
		s = not s
		print(s)

	def test_not(self):
		s = AtomicSentence(True, "p")
		print(s)

	def test_and(self):
		s = AtomicSentence(True, "p")
		a = s.cAnd(s)
		print(a)
	
	def test_or(self):
		s = AtomicSentence(True, "p")
		a = s.cOr(s)
		print(a)

	def test_imp(self):
		s = AtomicSentence(True, "p")
		a = s.cImp(s)
		print(a)

	def test_iff(self):
		s = AtomicSentence(True, "p")
		a = s.cIff(s)
		print(a)

if __name__ == '__main__':
    unittest.main(verbosity = 2)
