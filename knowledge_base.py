import copy

class KnowledgeBase:
	"""KnowledgeBase represents knowledge in CNF clauses"""
	def __init__(self, clauses):
		self.c = clauses

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

	def __eq__(self, clauses):
		return self.c == clauses

	def __str__(self):
		s = ""
		for clause in self.c:
			s += str([str(u) for u in list(clause)]) + "\n"
		return s

