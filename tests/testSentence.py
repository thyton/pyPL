import sys
sys.path.append('../../')
from pyPL.sentence import AtomicSentence
import unittest
import numpy as np 


class testSentence(unittest.TestCase):
	def test_table(self):
		print(AtomicSentence([True,False]).table())
	def test_condition(self):
		print(AtomicSentence().set(False).val())

if __name__ == '__main__':
    unittest.main()
