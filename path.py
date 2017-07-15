from collections import deque
from node import Node, distance

class Path:

	def __init__(self, _begin, _end, _nodes):	# _begin 	is the index of the node at which the wanted path begins
												# _end 		is the index of the node at which the wanted path ends
												# _nodes 	is the list (deque) of all nodes in the system

		# Assign params to object self
		self.start = _begin
		self.goal = _end
		self.nodes = _nodes

		self.pathNodes = deque()	# initializes path to an empty list (deque) of nodes

		# END ---------------

	def length(self):	# Returns the actual total length of all routes between nodes included in the path

		# Since each time a node is added to the path it inherits the G (travelled distance) from its parent _
		# and adds its own distance... this means that at the end, the final node in the path will have a G _
		# that equals the total distance travelled from the first start node to the final goal node

		return self.nodes[self.pathNodes[-1]].addToG()	# self.pathNodes[-1]	:: gives the index of the final node
														# .addToG()				:: returns the value of G

		# END ---------------

	def cost(self):		# Returns the total cost of the path (By adding all used routes' prices)

		total = 0	# initializes the variable with 0; it will contain the total cost at the end of the function

		for node in self.pathNodes:	# loops over all nodes node in the path
			if(self.nodes[node].getParent()!=None):	# makes sure that the current node is not the first node...
													# because the first node does not have a parent node...
													# and the cost from the origin to the first node (which equals the origin)...
													# is zero
				total += self.nodes[self.nodes[node].getParent()].getChildPrice()	#_
								# Adds the price of the route that leads to the current node from its parent.
								# [self.nodes[node].getParent()]	:: selects the parent node of the current node
								# .getChildPrice()					:: returns the price of the route from the selected ...
								# 									   ... node to its child node
		
		return total # Returns the final cost of the entire path

		# END ---------------

	def getPathIds(self):
		ids = []
		for _node in self.pathNodes:
			ids.append(_node)
		return ids

	def getPathNames(self):
		names = []
		for _node in self.pathNodes:
			names.append(self.nodes[_node].getName())
		return names

	def findPath(self):		# The main function which finds the best (shortest) possible path from the start node ...
							# to the end node; and returns the best path as a list (deque) of nodes
							# It uses A* algorithm with some modification
							# A* Pesudo Code is split as comments over corresponding parts of the function

		start = self.start 	# start is the index of the node that the path starts at
		goal = self.goal	# goal is the index of the node that the path is desired to end ar
		nodes = self.nodes 	# nodes is a list (deque) of all nodes in the system initialized

		# initialize the open list 
		openl = deque() 

		# initialize the closed list
		closel = deque()

		# put the starting node on the open list (you can leave its f at zero)
		nodes[start].open()
		openl.append(start)

		# while the open list is not empty
		while(len(openl)):
			# find the node with the least f on the open list, call it "q"
			q = openl[0]
			for i in openl:
				if(nodes[i].getF()<nodes[q].getF()):
					q = i
			# pop q off the open list
			openl.remove(q)
			nodes[q].ocNone()

		 #    generate q's 8 successors and set their parents to q
		 #    for each successor
		 #    	  if successor is the goal, stop the search
		 #        successor.g = q.g + distance between successor and q
		 #        successor.h = distance from goal to successor
		 #        successor.f = successor.g + successor.h

		 #        if a node with the same position as successor is in the OPEN list \
		 #            which has a lower f than successor, skip this successor
		 #        if a node with the same position as successor is in the CLOSED list \ 
		 #            which has a lower f than successor, skip this successor
		 #        otherwise, add the node to the open list
		 #    end
			for _child in nodes[q].child():
				child = _child[0]
				if(nodes[child].isclosed()==None):
					nodes[child].setParent(q)

				nodes[child].addToG(nodes[q].addToG())
				nodes[child].addToG(distance(nodes[q], nodes[child]))
				
				if(child == goal):
					openl.clear()
					break

				nodes[child].setH(nodes[goal])
				if(not(closel.count(child)>0)):
					openl.append(child)

			closel.append(q)
			nodes[q].close()

		if(nodes[goal].getParent()==None):
			return "No Path Found"

		path = deque([goal])
		parent = nodes[goal].getParent()
		nodes[parent].setChild(goal)
		while(parent!=None):
			path.appendleft(parent)
			if(nodes[parent].getParent() != None):
				nodes[nodes[parent].getParent()].setChild(parent)
			parent = nodes[parent].getParent()

		self.pathNodes = path
		return path