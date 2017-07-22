from collections import deque
from node import Node, distance
from path import Path
import database

d = database.Data()

# initialize nodes list
nodes = deque()

def loadNodes():
	nodes.clear()
	for n in d.getAll('nodes'):
		nodes.append(Node(n['x'], n['y'], n['name']))
		print(str(n['id'])+": "+n['name'])
		for r in d.seaSrc('routes', n['id']-1):
			nodes[r['parent']].child(r['child'], r['price'])

def getIdByName(_name):
	if(_name.isdigit()):
		return int(_name)
	for _node in nodes:
		if(_node.getName() == _name):
			return _node.getId()


# p = Path(2, 8, nodes)

# if(p.findPath()=="No Path Found"):
# 	print("No Path Found")
# else:
# 	print(p.length())
# 	print(p.cost())

loadNodes()