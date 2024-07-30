from flask import Flask
from fastapi import HTTPException
from typing import  Dict
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.post("/answer/")
async def get_answer(question_data: Dict[str, str]):
    if 'question_text' not in question_data:
        raise HTTPException(status_code=400, detail="Question text not provided")
    response = "Ran succefully"
    # Assuming milvus_retriver returns a dictionary, add 'response' parameter to it
    response_with_parameter = {'response': response}
    return response_with_parameter

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')