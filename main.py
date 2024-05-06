from flask import Flask, request, jsonify

import search

def buildApp():
	app = Flask(__name__)

	@app.route("/")
	def home():
		return "Home"

	@app.route("/search/<path:keypath>", methods= ['GET'])
	def addNewList(keypath):
		keys = str(keypath.split('/')[0])
		keys = keys.replace("_", " ")
		saida = search.procurar_string_em_arquivos(keys)
		print(saida)
		return jsonify({'matchs': saida})
	
	return app

if __name__ == "__main__":
	app = buildApp()
	app.run(debug=True)

