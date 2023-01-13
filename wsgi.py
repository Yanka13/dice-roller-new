# wsgi.py
import random
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({ 'roll': random.randint(1,6) })


@app.route('/wow')
def wow():
    return jsonify({'roll': 'wow'})
