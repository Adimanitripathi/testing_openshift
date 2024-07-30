from flask import Flask, request, jsonify
from typing import  Dict
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/answer/", methods=['POST'])
def get_answer():
    question_data = request.get_json()
    if not question_data or 'question_text' not in question_data:
        return jsonify({"detail": "Question text not provided"}), 400

    response = "Ran successfully"
    response_with_parameter = {'response': response}
    return jsonify(response_with_parameter)

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')