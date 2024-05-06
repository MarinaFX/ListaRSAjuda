from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/")
def home():
	return "Home"

@app.route("/addLista")
def addNewList():
	return "Add New Lista"

if __name__ == "__main__":
	app.run(debug=True)

