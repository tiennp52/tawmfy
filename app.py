import json, requests, sys
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
	# port = int(os.getenv('PORT', 8000))
	app.run(debug=False)
