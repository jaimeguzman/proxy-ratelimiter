import time
import random

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
PrometheusMetrics(app)


# Mock Endpoints

@app.route("/categories/MLA97994")
def hello():
    time.sleep(random.random() * 5)
    return "200 - category MLA97994",200

@app.route("/categories/ML1111")
def hello2():
    time.sleep(random.random() * 1.07)
    return "200 - category ML1111",200

@app.route("/one")
def first_route():
    time.sleep(random.random() * 0.2)
    return " OK ",200

@app.route("/two")
def the_second():
    time.sleep(random.random() * 0.4)
    return "OK",201

@app.route("/three")
def test_3rd():
    time.sleep(random.random() * 0.6)
    return "NO",200

@app.route("/four")
def fourth_one():
    time.sleep(random.random() * 0.8)
    return "NOK 404",404

@app.route("/ping")
def ping():
    return "PONG",429


@app.route("/error")
def oops():
    return ":(", 500


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)
