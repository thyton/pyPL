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
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()