from Server import app
from flask import request, jsonify, render_template
from Server import database


@app.route('/api', methods=['GET'])
def api():
    '''
    The api endpoint
    :return:
    '''

    response = database.get_items()
    return jsonify(response.replace("\"", "'")), 200

@app.route('/')
def home():
    return "Hello"

@app.route('/plot')
def plot():
    return render_template('plot.html')
