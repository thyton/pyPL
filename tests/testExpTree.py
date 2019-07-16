import sys
sys.path.append('../../')
import copy 

from pyPL.exp_tree import ExpTree
from pyPL.sentence import AtomicSentence
from pyPL.sentence import Sentence

import unittest
import numpy as np 

class testExpTree(unittest.TestCase):
	s = {'p', 'q', 'imp', 'p', 'not', 'r', 'or', 'iff'}

	def test_init(self):
		p = AtomicSentence(True, "p")
		not_p = ~p

		q = AtomicSentence(True, "q")
		h = not_p.cAnd(q)
		not_p = ~p
		print(not_p)
		i =  not_p.cOr(q)
		i = ~i
		j = h.cAnd(i)
		print(j)
		j = ~j
		j = ~j
		j = ~j
		j = ~j
		j = ~j
		# q = ~q
		et = ExpTree(j.pns)
		print(et)

	def test_inwardNot(self):
		p = AtomicSentence(True, "p")
		not_p = ~p

		q = AtomicSentence(True, "q")
		h = not_p.cAnd(q)
		not_p = ~p
		print(not_p)
		i =  not_p.cOr(q)
		i = ~i
		j = h.cAnd(i)
		print(j)
		j = ~j
		j = ~j
		j = ~j
		j = ~j
		j = ~j
		# q = ~q
		et = ExpTree(j.pns)
		print(et)

		et.root = et.root.inwardNot()
		print(et.root)

	def test_replaceIff(self):
		p = AtomicSentence(True, "p")
		not_p = ~p

		q = AtomicSentence(True, "q")
		h = not_p.cIff(q)
		not_p = ~p
		print(not_p)
		i =  not_p.cOr(q)
		i = ~i
		j = h.cIff(i)
		print(j)
		j = ~j
		j = ~j
		j = ~j
		j = ~j
		j = ~j
		# q = ~q
		et = ExpTree(j.pns)
		print(et)

		et.root= et.root.replaceIff()
		print(et)

	def test_replaceImp(self):
		p = AtomicSentence(True, "p")
		not_p = ~p

		q = AtomicSentence(True, "q")
		h = not_p.cImp(q)
		not_p = ~p
		print(not_p)
		i =  not_p.cOr(q)
		i = ~i
		j = h.cImp(i)
		print(j)
		j = ~j
		j = ~j
		j = ~j
		j = ~j
		j = ~j
		# q = ~q
		et = ExpTree(j.pns)
		print(et)

		et.root = et.root.replaceImp()
		print(et)

	def test_distOr(self):
		p = AtomicSentence(True, "p")
		not_p = ~p
		q = AtomicSentence(True, "q")
		h = not_p.cAnd(q)
		not_p = ~p
		print(not_p)
		s = AtomicSentence(True, "s")
		i =  not_p.cAnd(s)
		# i = ~i
		j = h.cOr(i)
		print(j)
		j = ~j
		j = ~j
		j = ~j
		j = ~j
		# q = ~q
		et = ExpTree(j.pns)
		print(et)
		et.root = et.root.distOr()
		print(et)

	def test_parseCNFClauses(self):
		p = AtomicSentence(True, "p")
		not_p = ~p
		q = AtomicSentence(True, "q")
		h = not_p.cOr(q)
		h = h.cOr(h)
		not_p = ~p
		print(not_p)
		s = AtomicSentence(True, "s")
		i =  not_p.cAnd(s)
		j = h.cAnd(i)
		k = copy.deepcopy(j)
		l = j.cAnd(k)
		print(l)
		et = ExpTree(l.pns)
		print(et)

		clauses = []
		clauses = et.root.parseCNFClauses(clauses, False)

		print("[")
		for clause in clauses:
			print(clause)
			for unit in clause:
				print(unit, end=" ")
			print()
		print("]")

	def test_cnf(self):
		p = AtomicSentence(True, "p")
		not_p = ~p
		q = AtomicSentence(True, "q")
		h = not_p.cOr(q)
		h = h.cIff(h)
		h = ~h
		h = h.cAnd(h)
		h = ~h
		h = ~h
		et = ExpTree(h.pns)
		print(et)

		clauses = []
		clauses = et.cnf()
		print(et)
		
		print("[")
		for clause in clauses:
			print(clause)
			for unit in clause:
				print(unit, end=" ")
			print()
		print("]")

if __name__ == '__main__':
    unittest.main(verbosity = 2)
