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

	def test_not(self):
		s = AtomicSentence(True, "p")
		notS = ~s
		print(s)
		print(notS)
		print(s)

if __name__ == '__main__':
    unittest.main(verbosity=2)