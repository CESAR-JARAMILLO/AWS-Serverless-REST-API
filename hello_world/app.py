import json
import boto3
from flask_lambda import FlaskLambda
from flask import request

app = FlaskLambda(__name__)
ddb = boto3.resource("dynamodb")
table = ddb.Table('students')



@app.route('/hello')
def index():
    data = {
        "message": "Hello, world!"
    }
    return (
        json.dumps(data),
        200,
        {'Content-Type': "application/json"}
    )
