from flask import Flask, jsonify, redirect
from flask_cors import CORS
import random
from . import quotearr
app = Flask(__name__)
CORS(app)


@app.route("/quote")
def get_quote():
    result = { "quote": random.choice(quotearr)}
    return jsonify(result)

@app.route("/")
def index():
    return redirect("/static/main.html")

