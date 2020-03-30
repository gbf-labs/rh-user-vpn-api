import requests
import json

from flask import Flask
from flasgger import Swagger
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)
Swagger(app)

from controllers.ovpn import ovpn

ovpn = ovpn.Ovpn()

# ROUTE
app.route('/ovpn', methods=['POST'])(ovpn.ovpn)

if (__name__ == "__main__"):
    app.run(host='0.0.0.0', port = 5000)
