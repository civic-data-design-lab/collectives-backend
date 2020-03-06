from Server import app
from flask import request, jsonify

@app.route('/test', methods=['POST'])
def Test():
    # parameters are in request.form
    print(request.form)

    response = {
        'code': 0,
        'msg': "msg",
        'data': ["Important data"]
    }
    return jsonify(response), 200