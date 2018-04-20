from flask import Flask, render_template
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route("/pokemon/<query>")
def pokemon(query):
	r = requests.get('http://pokeapi.co/api/v2/pokemon/'+query)
	info = r.json()
	#if isinstance(query, (int, long)):
	#	return "The pokemon with id " + query + " is " + info['name'];
	#else:
	#	print query
	#	return query + " has id " + info['id'];

	try:
		value = int(query)
		return "The pokemon with id " + query + " is " + info['name'] + "."
	except ValueError:
		return query + " has id " + str(info['id']) + "."
  	
if __name__ == '__main__':
    app.run()
