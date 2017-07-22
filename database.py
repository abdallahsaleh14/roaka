import dataset

# def add('table', dict()) 	:: adds dict() to table 'table'
# def rem('table', id) 		:: removes row with id from table 'table'
# def getAll('table') 		:: returns a list of all rows in table 'table'
# def seaSrc('table', src)	:: returns a list of all rows in table 'table' whose 'src' == src

class Data(object):
	def __init__(self):
		self.db = dataset.connect('sqlite:///db.db')

	def add(self, _table, _data):
		table = self.db[_table]
		user= User(username="username", password="password", carnumber="carnumber")
		table.insert(user.__dict__)
		return table.insert(_data) 

	def rem(self, _table, _id):
		self.db.query("DELETE FROM " + _table + " WHERE id=" + str(_id))

	def getAll(self, _table):
		return self.db.get_table(_table).all()

	def seaSrc(self, _table, _src):
		table = self.db[_table]
		return table.find(table.table.columns.parent == _src)

	def getUsers():
		table= db['users']
		dbUsers = table.all()
		enUsers= []
		for user in dbUsers:
		print user
		enUser = User(**user)
		enUser.password = ""
		enUsers.append(enUser)
	return enUsers



	def signin(username, password):
		table= db['users']
		user = table.find_one(userName=username)
		if(user != None):
		user = User(**user)
		if(password == user.password):
			user.password = ""
			return user
		else:
			return None
	else:
		return None



	def addUser(user):
		table = db['users']
		id = table.insert(user.__dict__)
		user = User(**(table.find_one(id=id)))
		if user != None:
		user.password=''
	return user

	def getUser(user_id):
		table = db['users']
		user = table.find_one(id=user_id)
		if(user != None):
			user = User(**user)
			user.password=""
			return user
		return None
