import sys

sys.path.append('../../')
from pyPL.sentence import AtomicSentence
from pyPL.sentence import Sentence

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
		s = -s
		print(s)

	def test_not(self):
		s = AtomicSentence(True, "p")

if __name__ == '__main__':
    unittest.main(verbosity = 2)
