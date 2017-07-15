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
		return table.insert(_data) 

	def rem(self, _table, _id):
		self.db.query("DELETE FROM " + _table + " WHERE id=" + str(_id))

	def getAll(self, _table):
		return self.db.get_table(_table).all()

	def seaSrc(self, _table, _src):
		table = self.db[_table]
		return table.find(table.table.columns.parent == _src)
