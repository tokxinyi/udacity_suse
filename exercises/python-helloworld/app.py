# Exercise
# Extend the Python Flask application with /status and /metrics endpoints, considering the following requirements:

# Both endpoints should return an HTTP 200 status code
# Both endpoints should return a JSON response e.g. {"user": "admin"}. (Note: the JSON response can be hardcoded at this stage)
# The /status endpoint should return a response similar to this example: result: OK - healthy
# The /metrics endpoint should return a response similar to this example: data: {UserCount: 140, UserCountActive: 23}


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Goodbye world!"

@app.route("/status")
def health_status():
    if ("successful"):
        return 'result: OK - healthy'
    else:
        return 'Error 500'

@app.route("/metrics")
def metrics():
    data = {
        "user": "admin",
        "UserCount" : 140,
        "UserCountActive": 23
    }

    return data



if __name__ == "__main__":
    app.run(host='0.0.0.0')
