# Exercise
# Extend the Python Flask application with /status and /metrics endpoints, considering the following requirements:

# Both endpoints should return an HTTP 200 status code
# Both endpoints should return a JSON response e.g. {"user": "admin"}. (Note: the JSON response can be hardcoded at this stage)
# The /status endpoint should return a response similar to this example: result: OK - healthy
# The /metrics endpoint should return a response similar to this example: data: {UserCount: 140, UserCountActive: 23}


from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    logging.info('Main request successful')
    return "Hello World! Goodbye world!"

@app.route("/status")
# my attempt
# def health_status():
#     if ("successful"):
#         return 'result: OK - healthy'
#     else:
#         return 'Error 500'

def healthCheck():
    response = app.response_class(
        response = json.dumps({"result":"OK - healthy"}),
        status = 200,
        mimetype = 'application/json'
    )
    logging.info('Status request successful')
    return response

@app.route("/metrics")
# my attempt
# def metrics():
#     data = {
#         "user": "admin",
#         "UserCount" : 140,
#         "UserCountActive": 23
#     }
#    return data

def metrics():
    response = app.response_class(
        response = json.dumps({"status":"success", "code":0, "data":{"UserCount": 40, "UserCountActive": 23}}),
        status = 200,
        mimetype = 'application/json'
    )
    logging.info('Metrics request successful')
    return response

if __name__ == "__main__":
    logging.basicConfig(filename = 'app.log', format='%(levelname)s:%(message)s', level=logging.DEBUG)
    app.run(host='0.0.0.0')
    
