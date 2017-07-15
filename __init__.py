from flask import Flask, render_template, redirect, request
# from database import Data
from collections import deque
import main
import json
import geo
from path import Path

app = Flask(__name__, static_url_path='/static', template_folder='templates')
#d = Data()


# Code goes here

def updateSystem():
	main.loadNodes()
	geo.setNodes(main.nodes)
	geo.update()

updateSystem()

@app.route('/addRoute', methods=['GET', 'POST'])
def addRoute():

	return main.d.add('routes', dict(
		parent= int(request.args.get('from'))-1,
		child= int(request.args.get('to'))-1,
		price= int(request.args.get('price'))))

	updateSystem()
	return ""

# END -----------------------

@app.route('/findPath', methods=['GET', 'POST'])
def findPath():

	src= geo.findNearNode()
	dst= main.getIdByName(request.args.get('to'))-1

	p = Path(src, dst, main.nodes)

	if(p.findPath()=="No Path Found"):
		return "No Path Found"
	else:
		resp = dict(
			cost= p.cost(),
			length= p.length(),
			ids= p.getPathIds(),
			names= p.getPathNames())
		return json.dumps(resp)

# END -----------------------

@app.route('/removeRoute', methods=['GET', 'POST'])
def removeRoute():

	_id = main.getIdByName(request.args.get('id'))
	main.d.rem('routes', _id)

	updateSystem()
	return ""

# END -----------------------

@app.route('/listRoutes')
def listRoutes():
	_nodes = []
	for n in main.d.getAll('nodes'):
		for r in main.d.seaSrc('routes', n['id']-1):
			_nodes.append(dict(id= r['id'], src= r['parent']+1, dst= r['child']+1, acor= dict(x= main.nodes[r['parent']].cor(0), y= main.nodes[r['parent']].cor(1)), bcor= dict(x= main.nodes[r['child']].cor(0), y= main.nodes[r['child']].cor(1))))
	return json.dumps(_nodes)

# END -----------------------

@app.route('/updateSystem')
def ups():
	updateSystem()
	return ""

# END -----------------------


if __name__ == "__main__":
	app.debug = True
	app.run(port=3000)