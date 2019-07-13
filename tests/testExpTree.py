import sys
sys.path.append('../../')

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
		q = not_p.cAnd(q)
		print(q)
		q = ~q
		q = ~q
		q = ~q
		q = ~q
		q = ~q
		# q = ~q
		et = ExpTree(q.pns)
		print(et)

		et_cnf = et.cnf()
		print(et_cnf)

if __name__ == '__main__':
    unittest.main(verbosity = 2)
