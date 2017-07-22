class User():
	id = 0
	username= ''
	password= ''
	carnumber= ''

	def __init__(self, id, username, password, carnumber):
		self.id = id
		self.username= username
		self.password= password
		self.carnumber= carnumber

	def __init__(self, **entries):
			self.__dict__.update(entries)

	def to_json(self):
		json = "{"
		json +="\"id\":"+str(self.id)+","
		json +="\"userName\":\""+unicode(self.userName)+"\","
		json +="\"password\":\""+unicode(self.password)+"\","
		json +="\"carnumber\":\""+unicode(self.carnumber)+"\""
		json +="}"
		return json
