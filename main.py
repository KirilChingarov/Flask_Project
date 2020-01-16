from flask import Flask
from flask import render_template, redirect, request, url_for, send_file

from user import User
from images import Image
from catagory import Catagory

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template("index.html", catagories=Catagory.all(), images=Image.all())
	elif request.method == 'POST':
		catagory = request.form['searchbar']
		cat_id = Catagory.find(catagory)
		if not cat_id:
			return redirect("/")
		else:
			return redirect(url_for("get_catagory_by_id", id=cat_id.id))


@app.route("/catagory/<int:id>")
def get_catagory_by_id(id):
	return render_template("index.html", catagories=Catagory.all(), images=Image.find_by_catagory(id))


@app.route("/image/<int:id>")
def get_image_by_id(id):
	return render_template("image.html", image=Image.find_by_id(id))


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
		
		return redirect("/register_success")


@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html")
	elif request.method == 'POST':
		username = request.form['Username']
		password = request.form['Password']
		user = User.find_user(username)
		if not user or not user.verify_password(password):
			return redirect("/login")
		return redirect("/login_success")
		
	

@app.route("/register_success")
def sign_in_success():
	return "Sign in successful!"


@app.route("/login_success")
def login_success():
	return "Log in successful!"


if __name__ == "__main__":
	app.run()
