#!flask/bin/python
import requests
from flask import Flask
import json

app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/')
def hello():
	req = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=200&offset=20')
	print("HTTP Status Code: " + str(req.status_code))
	print(req.headers)
	json_response = json.loads(req.content)
	return_str = ""
	i = 0
	for pokemon in json_response['results']:
		i = i + 1
		return_str = return_str + pokemon['name'] + "\n"
		print(pokemon['name'])
	return req.content
				
	
	
if __name__ == '__main__':
	app.run()

	
