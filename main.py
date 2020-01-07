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
		return render_template("registerForm/input.html")
	elif request.method == 'POST':
		values = (
			request.form['firstname'],
			request.form['lastname'],
			request.form['email'],
			User.hash_password(request.form['password1'])
		)
		User(*values).create()
		
		return redirect("/register_success")


@app.route("/register_success")
def sign_in_sucess():
	return "Sign in successful!"


if __name__ == "__main__":
	app.run()
