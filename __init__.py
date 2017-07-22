from flask import Flask, render_template, redirect, request
# from database import Data
from collections import deque
import main
import json
import geo
from path import Path
import base64

app = Flask(__name__, static_url_path='/static', template_folder='templates')
#d = Data()


# Code goes here

def updateSystem():
	main.loadNodes()
	geo.setNodes(main.nodes)
	geo.update()

updateSystem()



# END -----------------------

def error(msg):
	return "{ \"ERROR\" : \""+msg+"\"}"

@app.route("/signin", methods=['POST', 'GET'])
def signin():
	reply = "[500, \"Somthing went wrong in server\"]"
	if request.method == "GET":
		return error("ERROR: Not allowed method")
	if request.method == "POST":
		if request.is_json:
			username = request.get_json()['username']
			password = base64.b64encode(request.get_json()['password'])

			user = db.signIn(username, password)
			if(user != None):
				token = "TOKEN HERE TEMP"#db.createToken()
				code = 200
				reply = "[ " + str(code) +" ,"
				reply += "\"" + token +"\","
				reply += user.to_json() +"]"
			else:
				reply ='[404, "Username or Password is wrong"]'
		else:
			return error("ERROR: Request is not json")
	return reply
@app.route("/users/<user_id>", methods=['POST', 'GET'])
def user(user_id):
	reply = "[500, \"Somthing went wrong in server\"]"
	if request.method == "GET":
		return error("ERROR: Not allowed method")
	if request.method == "POST":
		user = db.getUser(user_id)
		code = 200
		reply = "[ " + str(code) +" ,"
		reply+= user.to_json()
		reply += "]"
	return reply

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





@app.route('/updateSystem')
def ups():
	updateSystem()
	return ""
@app.route("/signup", methods=['POST', 'GET'])
def signup():
	reply = "[500, \"Somthing went wrong in server\"]"
	if request.method == "GET":
		return error("ERROR: Not allowed method")
	if request.method == "POST":
		if request.is_json:
			
			userName = request.get_json()['userName']
			password = base64.b64encode(request.get_json()['password'])
			passwordConf = base64.b64encode(request.get_json()['passwordConf'])
			
			carnumber = request.get_json()['carnumber']

			if(password == passwordConf):
				user = db.getUserByUserName(userName)
				if(user == None):
					del request.get_json()['passwordConf']
					user = db.addUser(User (userName=userName,password=password,carnumber=carnumber))
					if(user != None):
						token = "TOKEN HERE TEMP"#db.createToken()
						code = 200
						reply = "[ " + str(code) +" ,"
						reply += "\"" + token +"\","
						reply += user.to_json() +"]"
					else:
						reply ='[500, "Error from server"]'
				else:
					reply = '[1062, "Error, Username is taken"]'
		else:
			return error("ERROR: Request is not json")
	return reply

# END -----------------------


if __name__ == "__main__":
	app.debug = True
	app.run(port=3000)