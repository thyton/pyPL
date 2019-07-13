from pyPL.connective import *
from pyPL.literal import Literal
import copy

class Node:
	"""Node has root as the operator or Literal if there's no operation, 
	   left subtree and right subtree are operands
	   When the operator is Conn.NOT, there's no coresponding right subtree
	"""
	def __init__(self, **kwds):
		self.__dict__.update(kwds)

	def __str__(self, level=0):
		ret = "\t"*level+str(level)+": "+str(self.root)+"\n"
		if hasattr(self, 't1'):
			ret += self.t1.__str__(level+1)
		if hasattr(self, 't2'):
			ret += self.t2.__str__(level+1)
		return ret

	def __repr__(self, level=0):
		ret = "\t"*level+str(level)+": "+repr(self.root)+"\n"
		if hasattr(self, 't1'):
			ret += self.t1.__repr__(level+1)
		if hasattr(self, 't2'):
			ret += self.t2.__repr__(level+1)
		return ret

	def clone(self):
		cp = copy.deepcopy(self)
		return cp

	def replaceIff(self):
		if self.root:
			return

	def replaceImp(self):
		return

	def inwardNeg(self):
		if isinstance(self.root, Conn):
			if hasattr(self, 't1'): 
				if isinstance(self.t1.root, Conn) and self.root == Conn.NOT:
					if self.t1.root == Conn.NOT: 
						self = self.t1.t1 
						self = self.elim2Neg()
					elif self.t1.root == Conn.AND:
						print(type(self.t1.root))
						print(self.root)
						print(self.t1.root)
						print(type(self.t1.t1))
						self.t1.root = Conn.OR
						d = {'t1':self.t1.t1,'root':Conn.NOT}
						self.t1.t1 = Node(**d)
						d = {'t1':self.t1.t2,'root':Conn.NOT}
						self.t1.t2 = Node(**d)
						self = self.t1 
						self = self.elim2Neg()
					else:
						self.t1.root = Conn.AND
						d = {'t1':self.t1.t1,'root':Conn.NOT}
						self.t1.t1 = Node(**d)
						d = {'t1':self.t1.t2,'root':Conn.NOT}
						self.t1.t2 = Node(**d)
						self = self.t1 
						self = self.elim2Neg()
				else:
					self.t1.elim2Neg()	

			if hasattr(self, 't2'):
				self.t2.elim2Neg()				
		return self

		return

	def elim2Neg(self):
		if isinstance(self.root, Conn):
			if hasattr(self, 't1'): 
				if isinstance(self.t1.root, Conn) and self.root == Conn.NOT and self.t1.root == Conn.NOT: 
					# print(type(self.t1.root))
					# print(self.root)
					# print(self.t1.root)
					# print(type(self.t1.t1))
					self = self.t1.t1 
					self = self.elim2Neg()
				else:
					self.t1.elim2Neg()	

			if hasattr(self, 't2'):
				self.t2.elim2Neg()				
		return self

class ExpTree:
	def __init__(self, pns):
		stack = []
		i = 0
		while i < len(pns):
			if not isinstance(pns[i], Conn):
				d = {'root':pns[i]}
			elif pns[i] == Conn.NOT:
				t1 = stack.pop()
				d = {'t1':t1,'root':pns[i]}
			else :
				t2 = stack.pop()
				t1 = stack.pop()
				d = {'t1':t1, 't2':t2, 'root':pns[i]}

			node = Node(**d)
			stack.append(node)	
			i += 1
		self.root = node

	def cnf(self):
		self.root = self.root.elim2Neg()
				 # = Literal(True, "s")
		return self

	def __str__(self):
		return str(self.root)

	def __repr__(self):
		return repr(self.root)
	