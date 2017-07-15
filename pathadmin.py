from database import Data
from node import Node
from collections import deque

# Add Path, Remove Path, Extract Nodes with children (paths), Add Nodes

class PathAdmin:

	def __init__(self, db): # db is the database which this panel will work on. db is of type Data
		self.db = db


	def addPath(self, src, dst, cost): # Creates a path between two nodes (two cities) as driver requests
		return self.db.add('paths', dict(src=src, dst= dst, cost= cost)) # _
											# Adds the new path as a new row to server's database
											# and returns the id of the new row
											# The id can be used laterly to remove the path
		# END ------------------

	def remPath(self, _id): # Removes a path from the database given its id (The one returned from the last function)
		self.db.rem('paths', _id)	# Removes the row corresponding to the path that its id is provided
									# The id is the number returned from the addPath function
		# END ------------------
	
	def addNode(self, _x, _y, _name="Common Point"): # Creates a node (city)
		return self.db.add('nodes', dict(x=_x, y= _y, name= _name)) # _
											# Adds the new node as a new row to server's database
											# and returns the id of the new row
		# END ------------------

	def extractNodes(self): # Returns a list with type (deque) which has elements of type (Node)
							# The list includes all nodes (cities) added to the dataset
		nodes = deque()	# Creates an empty variable of type deque (list)
		for _node in self.db.getAll('nodes'):	# loops over all rows in table 'nodes' as _node
			nodes.append(Node(_node['x'], _node['y'], _name=_node['name']))	# _
											# Creates a new object of type Node
											# Node's first param is the x coordinate of the point (city)
											# Node's secon param is the y coordinate of the point (city)
			
			# Adding child nodes: (Based on paths)
			for _path in self.db.seaSrc('paths', len(nodes)-1):	# loops over all paths whose src is _node
				nodes[-1].child(_path['dst'], _path['cost'])	# Selects the last element in nodes (=_node)
																# Adds current _path's dst as a child to _node
																# Sets the price of the child (path) to _path's cost

		return nodes 	# Returns variable 'nodes' of type deque (list)...
						# it includes all saved points (cities) of type Node
		# END ------------------