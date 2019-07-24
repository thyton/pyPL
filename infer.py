import copy

def toTuple(clause):
	unitSet = set()
	for unit in clause:
		unitSet.add(unit)
	return tuple(unitSet)

def resolve(c1, c2):
	"""A resolution algorithm for propositional logic. 
	Return all possible clauses resolved from c1 and c2 
	c1: a tuple of units
	c2: a tuple of units
	"""
	res = set()
	c1Set = set(c1)
	for unit in c2:
		unit_copy = ~copy.deepcopy(unit)
		c1List = list(c1)
		if unit_copy in c1Set:
			c1List.remove(unit_copy)
			# compute resolvent
			resolvent = set(c1List)
			c2ResSet = set([u for u in c2 if not u == unit])
			resolvent = resolvent.union(c2ResSet)
			res.add(tuple(resolvent))
	return res

def resolution(kb, a):
	"""A resolution algorithm for propositional logic.
	Return if kb entails a
	
	Each pair that contains complementary literals is resolved to produce a new clause.
	The new clause is added to the knowledge base if not already present.
	The algorithm halts 
		- when there are no new claused that can be added. 
			KB doesn't entail a 
		- or when two clauses resolve to yield the empty clause
			KB entails a
	"""
	clauses = kb.clauses().union((~copy.deepcopy(a)).cnf())	
	new = set()
	while(True):
		for c1 in clauses:
			for c2 in clauses:
				if c1 is not c2:
					resolvents = resolve(c1, c2)
					if () in resolvents:
						return True
					new = new.union(resolvents)	

		isNewSubset = True
		for c in new:
			if not c in clauses:
	 			isNewSubset = False
		
		if isNewSubset: 
			return False
		else:
			clauses = clauses.union(new)












