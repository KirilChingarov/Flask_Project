from database import DB

class Catagory:
	def __init__(self, id, name):
		self.id = id
		self.name = name
	
	@staticmethod
	def all():
		with DB() as db:
			rows = db.execute('SELECT * FROM catagories').fetchall()
			return [Catagory(*row) for row in rows]
	
	@staticmethod
	def find(catagory):
		with DB() as db:
			row = db.execute('SELECT * FROM catagories WHERE name = ?', (catagory,)).fetchone()
			if not row:
				return None
			return Catagory(*row)
	
	@staticmethod
	def find_by_id(id):
		with DB() as db:
			row = db.execute('SELECT * FROM catagories WHERE id = ?', (id,)).fetchone()
			if not row:
				return None
			return Catagory(*row)
