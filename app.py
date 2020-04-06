#import files
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
	user_input = request.args.get('msg')

	vocab = ["oof", "rip", "yee", "f"]

	vocab_i = vocab[random.randint(0,3)]
	input_word = user_input.split()[random.randint(0,len(user_input.split()) - 1)]

	response = input_word + " " + vocab_i

	return response
	
if __name__ == "__main__":
	app.run()