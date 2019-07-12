import sys
sys.path.append('../../')

from pyPL.sentence import *

class PNS:
	def pr(l):
		return [str(i) for i in l]
	def replaceIff(s, stack, o):
		"""Replace p Iff q by (p implies q) and (q implies p)
		in postfix notation string
		self: a pns list
		p:  [start index, end index) of p
		q:  [start index, end index) of q
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
		self: a pns list
		p:  [start index, end index) of p
		q:  [start index, end index) of q
		o:  iff index 
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

	def inwardNot(s, stack, o):
		"""Replace not p by negative literal not p
		self: a pns list
		p:  [start index, end index) of p
		o:  iff index 

		Applying De Morgan's Law when needed
		"""

	def distOr(s, stack, o):
		"""Distribute or over and"""

	def combineOperands(s, stack, o):
		"""Distribute or over and"""
		try:
			p = stack.pop()
			if s[o] != Conn.NOT:
				p = stack.pop()
			stack.append((p[0], o+1))
		except:
			print("Empty Stack")