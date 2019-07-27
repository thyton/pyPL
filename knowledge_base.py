import copy

class KnowledgeBase:
	"""KnowledgeBase represents knowledge in CNF clauses"""
	def __init__(self, clauses):
		self.c = clauses
		self.resolved = set()

	def add(self, clause):
		self.c.add(clause)
		return self

	def extend(self, resolvents):
		for r in resolvents:
			self.c.add(r)
		return self

	def has(self, clause):
		return clause in self.c

	def clauses(self):
		return copy.deepcopy(self.c)

	def resolve(self, c1, c2):
		return tuple([c1, c2]) in self.resolved or tuple([c2,c1]) in self.resolved

	def markResolved(self, c1, c2):
		return self.resolved.add(tuple([c1,c2]))

	def __eq__(self, clauses):
		return self.c == clauses

	def __str__(self):
		s = ""
		for clause in self.c:
			s += str([str(u) for u in list(clause)]) + "\n"
		return s

