import sys
sys.path.append('../../')

from pyPL.sentence import AtomicSentence
from pyPL.sentence import Sentence

import unittest
import numpy as np 

class testSentence(unittest.TestCase):
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

	def test_combination(self):
		p = AtomicSentence(True, "p")
		not_p = ~p
		print(p)
		print(not_p)

		q = AtomicSentence(True, "q")
		p_imp_q = p.cImp(q)
		print(p_imp_q)

		r = AtomicSentence(True, "r")
		n_p_or_r = not_p.cOr(r)
		print(n_p_or_r)

		print(p_imp_q.cIff(n_p_or_r))

	def test_replaceIff(self):
		p = AtomicSentence(True, "p")
		not_p = ~p

		q = AtomicSentence(True, "q")
		p_imp_q = p.cImp(q)

		r = AtomicSentence(True, "r")
		n_p_or_r = not_p.cOr(r)

		s = p_imp_q.cIff(n_p_or_r)
		print(s)
		s.replaceIff()
		print(s)


	def test_replaceImp(self):
		p = AtomicSentence(True, "p")
		not_p = ~p

		q = AtomicSentence(True, "q")
		p_iff_q = p.cIff(q)

		r = AtomicSentence(True, "r")
		n_p_or_r = not_p.cOr(r)

		s = p_iff_q.cImp(n_p_or_r)
		print(s)
		s.replaceImp()
		print(s)	

	def test_inwardNot(self):
		p = AtomicSentence(True, "p")
		not_p = ~p

		q = AtomicSentence(True, "q")
		q = not_p.cAnd(q)
		print(q)
		q = ~q
		q = ~q
		q = ~q
		q_cnf = q.cnf()
		
		print(repr(q_cnf))
		# print(q)
		# q.inwardNot()
		# print(q)

		# not_p = ~p
		# q = AtomicSentence(True, "q")
		# q = not_p.cOr(q)
		# print(q)
		# q = ~q
		# print(q)

		# s.replaceImp()
		# print(s)	
if __name__ == '__main__':
    unittest.main(verbosity = 2)
