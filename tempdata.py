from database import *
from collections import deque
from node import Node

d = Data()


# ## Used to load data into deque
# # initialize nodes list
# nodes = deque()

# for n in d.getAll('nodes'):
# 	nodes.append(Node(n['x'], n['y'], n['name']))
# 	for r in d.seaSrc('routes', n['id']-1):
# 		nodes[r['parent']].child(r['child'])

# d.rem('routes', 13b)

# print(d.add('routes', dict(
# 	parent= 6,
# 	child= 10,
# 	price= 4)))

for n in d.getAll('routes'):
	print(str(n['id']) + ": " + str(n['parent'])+" >> " + str(n['child']) + " :: " + str(n['price']))


### Used to import nodes to the DB

# for n in nodes:
# 	d.add('nodes', dict(
# 		x= n.cor(0),
# 		y= n.cor(),
# 		name= n.getName()))



### Used to add temp routes

# def ne(a, b, p=0):
# 	d.add('routes', dict(
# 		parent= a,
# 		child= b,
# 		price= p))

# ne(2,0, 10)
# ne(0, 2,1)
# ne(1,3, 4)
# ne(1,3, 2)
# ne(3, 2,2)
# ne(2,5,4)
# ne(1,4, 2)
# ne(4,3, 2)
