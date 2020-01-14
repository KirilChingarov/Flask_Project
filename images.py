from database import DB

class Image:
	def __init__(self, id, name, catagory):
		self.id = id
		self.name = name
		self.catagory = catagory
	
	@staticmethod
	def all():
		with DB() as db:
			rows = db.execute('SELECT * FROM images').fetchall()
			return [Image(*row) for row in rows]

	@staticmethod
	def find_by_catagory(catagory):
		with DB() as db:
			rows = db.execute('SELECT * FROM images WHERE catagory = ?', (catagory,)).fetchall()
			if not rows:
				return None
			return [Image(*row) for row in rows]
	
	def printInfo(self):
		print(self.id)
		print(self.name)
		print(self.catagory)
		print("-------")
