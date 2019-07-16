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
		"""Replace all α IFF β by (α IMP β) AND (β IMP α) """
		if isinstance(self.root, Conn):
			# when root is IFF	
			if self.root == Conn.IFF:
				self.root = Conn.AND
				d = {'t1':self.t1.clone(),'root':Conn.IMP,'t2':self.t2.clone()}
				newT1 = Node(**d)
				d = {'t1':self.t2.clone(),'root':Conn.IMP,'t2':self.t1.clone()}
				self.t2 = Node(**d)
				self.t1 = newT1
				self = self.replaceIff()
			else:
			# when root isn't IFF	
				self.t1 = self.t1.replaceIff()	
			if hasattr(self, 't2'):
				self.t2 = self.t2.replaceIff()			
		return self

	def replaceImp(self):
		""" Replace all α IMP β by not α OR β """
		if isinstance(self.root, Conn):
			# when root is IMP	
			if self.root == Conn.IMP:
				self.root = Conn.OR
				d = {'t1':self.t1,'root':Conn.NOT}
				self.t1= Node(**d)
				self = self.replaceImp()
			else:
			# when root isn't IMP
				self.t1 = self.t1.replaceImp()	
			if hasattr(self, 't2'):
				self.t2 = self.t2.replaceImp()			
		return self

	def inwardNot(self):
		""" Move NOT inwards
			NOT NOT α = α 
			Apply De Morgan's Law to NOT (α OR β) , NOT (α AND β)"""
		if isinstance(self.root, Conn):
			# when the root is NOT
			if self.root == Conn.NOT:
				if isinstance(self.t1.root, Conn):
					# 2 consecutive NOTs
					if self.t1.root == Conn.NOT: 
						self = self.t1.t1 
						self = self.inwardNot()
					# NOT - AND using De Morgan's Law	
					elif self.t1.root == Conn.AND:
						self.t1.root = Conn.OR
						d = {'t1':self.t1.t1,'root':Conn.NOT}
						self.t1.t1 = Node(**d)
						d = {'t1':self.t1.t2,'root':Conn.NOT}
						self.t1.t2 = Node(**d)
						self = self.t1 
						self = self.inwardNot()
					# NOT - OR using De Morgan's Law	
					else:
						self.t1.root = Conn.AND
						d = {'t1':self.t1.t1,'root':Conn.NOT}
						self.t1.t1 = Node(**d)
						d = {'t1':self.t1.t2,'root':Conn.NOT}
						self.t1.t2 = Node(**d)
						self = self.t1 
						self = self.inwardNot()
			else:
			# when root isn't NOT	
				self.t1 = self.t1.inwardNot()	
				self.t2 = self.t2.inwardNot()			
		return self

	def distOr(self):
		""" Distribute OR over AND using Distributivity Law """
		if isinstance(self.root, Conn):
			# when the root is OR
			if self.root == Conn.OR:
				# root - left subtree = OR - AND using Distributivity Law
				if isinstance(self.t1.root, Conn) and self.t1.root == Conn.AND:
					self.root = Conn.AND
					d = {'t1':self.t1.t1.clone(),'root':Conn.OR, 't2':self.t2.clone()}
					newT1 = Node(**d)
					d = {'t1':self.t1.t2.clone(),'root':Conn.OR, 't2':self.t2.clone()}
					self.t2 = Node(**d)
					self.t1 = newT1

				elif isinstance(self.t2.root, Conn) and self.t2.root == Conn.AND:
					self.root = Conn.AND
					d = {'t1':self.t1.clone(), 'root':Conn.OR, 't2':self.t2.t1.clone()}
					newT1 = Node(**d)
					d = {'t1':self.t1.clone(), 'root':Conn.OR, 't2':self.t2.t2.clone()}
					self.t2 = Node(**d)
					self.t1 = newT1

			# recursively call it one subtrees
			self.t1 = self.t1.distOr()	
			if hasattr(self, 't2'):
				self.t2 = self.t2.distOr()			
		
		return self

	def parseCNFClauses(self, clauses, isRootOR):
		""" Return a list of conjunctive clauses
			Each clause is a list of literals
			Assumming the calling object is in CNF, that there're 3 operators NOT, AND, OR
		"""
		if isinstance(self.root, Conn):				
			if self.root == Conn.AND:
				leftClauses = self.t1.parseCNFClauses([], isRootOR)
				rightClauses = self.t2.parseCNFClauses([], isRootOR)
				clauses.extend(leftClauses)
				clauses.extend(rightClauses)
				return clauses
			elif self.root == Conn.OR:
				if isRootOR:
					return self.t1.parseCNFClauses([], isRootOR) + self.t2.parseCNFClauses([], isRootOR)
				else:
					isRootOR = True
					return [self.t1.parseCNFClauses([], isRootOR) + self.t2.parseCNFClauses([], isRootOR)]
			else:
				if isRootOR:
					return [~copy.deepcopy(self.t1.root)]
				else:
					return [[~copy.deepcopy(self.t1.root)]]
		else:
			if isRootOR:
				return [copy.deepcopy(self.root)]
			else:
				return [[copy.deepcopy(self.root)]]


class ExpTree:
	def __init__(self, pns):
		if len(pns) > 0:
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
		else:
			self = None

	def cnf(self):
		self.root = self.root.replaceIff()
		self.root = self.root.replaceImp()
		self.root = self.root.inwardNot()
		self.root = self.root.distOr()
		clauses = []	
		clauses = self.root.parseCNFClauses(clauses, False)
		clauseSet = set()
		for clause in clauses:
			unitSet = set()
			for unit in clause:
				unitSet.add(unit)
			unitSet = tuple(unitSet)
			clauseSet.add(unitSet)
		return clauseSet

	def __str__(self):
		return str(self.root)

	def __repr__(self):
		return repr(self.root)
	