import sys
sys.path.append('../../')

from pyPL.sentence import *

class PNS:
	def pr(l):
		return [str(i) for i in l]

	def replaceIff(s, stack, o):
		"""Replace p Iff q by (p implies q) and (q implies p)
		in postfix notation string
		s: a pns list
		stack: stack of operands before o
		o:  iff index 
		"""
		q = stack.pop()
		p = stack.pop()
		r = [] # replacement
		r += s[p[0]:p[1]]
		r += s[q[0]:q[1]]
		r.append(Conn.IMP)
		r += s[q[0]:q[1]]
		r += s[p[0]:p[1]]
		r.append(Conn.IMP)
		r.append(Conn.AND)
		# pair(start, end) of the replacement clause
		i = (p[0], p[0] + len(r))
		s[p[0]:o+1] = r
		stack.append(i)

	def replaceImp(s, stack, o):
		"""Replace p Imp q by (not p or q)
		in postfix notation string
		s: a pns list
		stack: stack of operands before o
		o:  imp index 
		"""
		q = stack.pop()
		p = stack.pop()
		r = [] # replacement
		r += s[p[0]:p[1]]
		r.append(Conn.NOT)
		r += s[q[0]:q[1]]
		r.append(Conn.OR)

		# pair[start, end) of the replacement clause
		i = (p[0], p[0] + len(r))
		s[p[0]:o+1] = r
		stack.append(i)

	def elim2Neg(s, stack, o):
		"""Replace not p by negative literal not p
		s: a pns list
		stack: stack of operands before o
		o: right most operator NOT index 
		"""
		s.pop(o)
		s.pop(o)

	def deMorgan(s, stack, o, connective):
		"""Apply De Morgan's Law 
		s: a pns list
		stack: stack of operands before o
		o: current operator index 
		connective: the resulting connective after De Morgan
		"""
		q = stack.pop()
		p = stack.pop()
		r = [] # replacement
		r += s[p[0]:p[1]]
		r.append(Conn.NOT)
		r += s[q[0]:q[1]]
		r.append(Conn.NOT)
		r.append(connective)
		s[p[0]:o+1] = r
		i = (p[0], p[0] + len(r))
		stack.append(i)

	def toNegLiteral(s, stack, o):	
		"""Apply De Morgan's Law 
		s: a pns list
		stack: stack of operands before o
		o: current operator index 
		connective: the resulting connective after De Morgan
		"""
		s[p[0]] = ~s[p[0]]
		s.pop(o)
		stack.append(i)

	def distOr(s, stack, o):
		"""Distribute or over and
		s: a pns list
		stack: stack of operands before o
		o: or index 
		"""

	def combineOperands(s, stack, o):
		"""Distribute or over and"""
		try:
			p = stack.pop()
			if s[o] != Conn.NOT:
				p = stack.pop()
			stack.append((p[0], o+1))
		except:
			print("Empty Stack")