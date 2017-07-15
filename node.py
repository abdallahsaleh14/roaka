import math
from collections import deque

def distance(a, b): # returns the PHYSICAL distance between two Nodes
	return math.sqrt((a.cor(0)-b.cor(0))**2 + (a.cor()-b.cor())**2)

class Node:

	def __init__(self, x, y, _name="Common Point", _id=None):
		self._id = _id

		self.children = deque() # Children indices

		self._child = None
		self.parent = None
		self.closed = None

		self.x = x
		self.y = y
		self.name = _name

		self.g = 0 # Passed distance
		self.h = 0 # heuristic
		self.f = 0 # cost (total)

	def cor(self, v=1):
		if(v == 0): return self.x
		else: return self.y

	def setChild(self, __child):
		self._child = __child

	def setParent(self, _parent):
		self.parent = _parent

	def getChild(self):
		return self._child

	def getChildPrice(self):
		for __child in self.children:
			if(__child[0] == self._child):
				return __child[1]
		return 0

	def getId(self):
		return self._id
		
	def getParent(self):
		return self.parent

	def addToG(self, v=0):
		self.g = self.g + v
		self.f = self.g + self.h
		return self.g

	def getF(self):
		self.f = self.g + self.h
		return self.f

	def setH(self, tar):
		self.h = distance(self, tar)
		self.f = self.g + self.h
		return self.h

	def open(self):
		self.closed = False
	def close(self):
		self.closed = True
	def ocNone(self):
		self.closed = None
	def isclosed(self):
		return self.closed

	def getName(self):
		return self.name
		
	def child(self, _child=None, _price=0):
		if(_child != None):
			self.children.append((_child, _price))
		return self.children