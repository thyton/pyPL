import sys
sys.path.append('../../')
import copy 

from pyPL.exp_tree import ExpTree
from pyPL.sentence import AtomicSentence
from pyPL.sentence import Sentence
from pyPL.knowledge_base import KnowledgeBase
from pyPL.infer import *
import unittest
import numpy as np 

class testKnowledgeBase(unittest.TestCase):
	def __printClauses__(self, clauses):
		for clause in clauses:
			print(str([str(u) for u in list(clause)]))

	def test_init(self):
		print()
		p = AtomicSentence(True, "p")
		q = AtomicSentence(True, "q")
		s = q.cImp(p).cAnd(~q)
		s_cnf = s.cnf()
		self.__printClauses__(s_cnf)
		s_kb = KnowledgeBase(s_cnf)

		print("Resolution with ", p, resolution(s_kb, p))

		p = AtomicSentence(True, "p")
		q = AtomicSentence(True, "q")
		s = q.cImp(p).cAnd(q)
		s_cnf = s.cnf()
		self.__printClauses__(s_cnf)
		s_kb = KnowledgeBase(s_cnf)

		print("Resolution with ", p,resolution(s_kb, p))

if __name__ == '__main__':
    unittest.main(verbosity = 2)