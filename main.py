from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
	return redirect("/sign_in")


@app.route("/sign_in")
def sing_in():
	return render_template("registerForm/input.html")


if __name__ == "__main__":
	app.run()
