from flask import Flask
from flask import render_template, redirect, request

from user import User

app = Flask(__name__)

@app.route("/")
def home():
	return redirect("/register")


@app.route("/register", methods=['GET', 'POST'])
def sing_in():
	if request.method == 'GET':
		return render_template("register.html")
	elif request.method == 'POST':
		values = (
			request.form['Username'],
			request.form['E-Mail'],
			User.hash_password(request.form['Password'])
		)
		User(*values).create()
		
		return redirect("/register_success")


@app.route("/register_success")
def sign_in_sucess():
	return "Sign in successful!"


if __name__ == "__main__":
	app.run()
