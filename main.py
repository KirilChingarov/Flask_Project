from flask import Flask
from flask import render_template, redirect, request

from user import User
from images import Image

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html", images=Image.all())


@app.route("/register", methods=['GET', 'POST'])
def sing_in():
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
