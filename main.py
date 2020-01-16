from flask import Flask
from flask import render_template, redirect, request, session, url_for, send_file

import logging
from logging.handlers import RotatingFileHandler

from user import User
from images import Image
from catagory import Catagory

app = Flask(__name__)

app.secret_key = '6523e58bc0eec42c31b9635d5e0dfc23b6d119b73e633bf3a5284c79bb4a1ede'

logging.basicConfig(filename='logs.log', level=logging.INFO)

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
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
		session['username'] = request.form['username']
		
		return redirect("/")


@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html")
	elif request.method == 'POST':
		username = request.form['Username']
		password = request.form['Password']
		user = User.find_user(username)
		if not user or not user.verify_password(password):
			logging.error("%s failed to log in" % username)
			return redirect("/login")
		session['username'] = username
		logging.info("%s logged in successfully" % username)
		return redirect("/")
		
	
@app.route("/logout")
def logout():
	user = session['username']
	session.pop('username', None)
	logging.info("%s logged out successfully")
	return redirect("/")



if __name__ == "__main__":
	app.run()
