from flask import Flask
from flask import render_template, redirect, request, session, url_for

from logger import infolog, errorlog

from user import User
from images import Image
from catagory import Catagory

app = Flask(__name__)

app.secret_key = '6523e58bc0eec42c31b9635d5e0dfc23b6d119b73e633bf3a5284c79bb4a1ede'


@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		session['last_page'] = "/"
		if 'username' in session:
			return render_template("index.html", user=session['username'], catagories=Catagory.all(), images=Image.all())
		return render_template("index.html", user=None, catagories=Catagory.all(), images=Image.all())
	elif request.method == 'POST':
		catagory = request.form['searchbar']
		cat_id = Catagory.find(catagory)
		if not cat_id:
			return redirect("/")
		else:
			return redirect(url_for("get_catagory_by_id", id=cat_id.id))


@app.route("/catagory/<int:id>")
def get_catagory_by_id(id):
	if 'username' in session:
		return render_template("index.html", user=session['username'], catagories=Catagory.all(), images=Image.find_by_catagory(id))
	return render_template("index.html", user=None, catagories=Catagory.all(), images=Image.find_by_catagory(id))


@app.route("/image/<int:id>")
def get_image_by_id(id):
	if 'username' in session:
		return render_template("image.html", image=Image.find_by_id(id))
	session['last_page'] = "image/" + str(id)
	return redirect("/login")


@app.route("/register", methods=['GET', 'POST'])
def sign_in():
	if request.method == 'GET':
		return render_template("register.html")
	elif request.method == 'POST':
		values = (
			None,
			request.form['username'],
			request.form['email'],
			User.hash_password(request.form['password'])
		)
		User(*values).create()
		session['username'] = request.form['username']
		infolog.info("%s registered successfully", request.form['username'])
		
		return redirect(session['last_page'])


@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html", wrong_combo=False)
	elif request.method == 'POST':
		username = request.form['Username']
		password = request.form['Password']
		user = User.find_user(username)
		if not user or not user.verify_password(password):
			errorlog.error("%s failed to log in", username)
			return render_template("login.html", wrong_combo=True)
		session['username'] = username
		infolog.info("%s logged in successfully", username)
		return redirect(session['last_page'])
		
	
@app.route("/logout")
def logout():
	user = session['username']
	session.pop('username', None)
	infolog.info("%s logged out successfully", user)
	return redirect("/")



if __name__ == "__main__":
	app.run()
