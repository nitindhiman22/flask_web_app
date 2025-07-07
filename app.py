from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
	return "i am nitin dhiman"

@app.route("/phone")
def lwphone():
	return "9808580941"

app.run(host="0.0.0.00")