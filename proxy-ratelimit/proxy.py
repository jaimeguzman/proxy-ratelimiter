from distutils.log import debug
import requests
from requests import get
from requests.exceptions import Timeout
from requests.exceptions import HTTPError
from flask import Flask,request
import flask_limiter
from flask_limiter import ExemptionScope, Limiter
from flask_limiter.util import get_remote_address



SITE_NAME = 'http://api.mercadolibre.com:5000/'


app = Flask('__main__')


def index_error_responder(request_limit):
    error_template = jinja2.Environment().from_string(
        """
    <h1>Breached rate limit of: {{request_limit.limit}}</h1>
    <h2>Path: {{request.path}}</h2>
    """
    )
    return make_response(render_template(error_template, request_limit=request_limit))

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["2 per minute", "1 per second"],
    storage_uri="memory://",
    # Redis
    # storage_uri="redis://localhost:6379",
    # Redis cluster
    # storage_uri="redis+cluster://localhost:7000,localhost:7001,localhost:70002",
    # Memcached
    # storage_uri="memcached://localhost:11211",
    # Memcached Cluster
    # storage_uri="memcached://localhost:11211,localhost:11212,localhost:11213",
    # MongoDB
    # storage_uri="mongodb://localhost:27017",
    strategy=  "moving-window",  #"fixed-window", # or "moving-window"
)


# Para poder soportar 55.000 req/sec = tendremos una equivalente 3.000.000 por minituo.
# Rate Limit settings

# proxy decorators
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@limiter.limit("700/minute", on_breach=index_error_responder)
def proxy(path):

    url = f'{SITE_NAME}{path}'
    response = requests.get( url )

    return get(f'{SITE_NAME}{path}').content,response.status_code



app.run(host='0.0.0.0' ,debug=True, port=8080)



