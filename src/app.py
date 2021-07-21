from unittest import result

import bottle
import json
import logging
from datetime import datetime

from flask import Flask

from src.custom_logger import console_logger

console_logger()
# app = bottle.Bottle()
app = Flask(__name__)
now = datetime.now()

logger = logging.getLogger(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello():
    return "Hello World!"


@app.route('/status', methods=['POST', 'GET'])
def h_check():
    response = {}
    headers = {'Content-type': 'application/json'}
    response['status'] = "Success"
    response['message'] = {'result': 'OK - Healthy'}
    result = json.dumps(response)
    logger.info(f"h_check endpoint was reached")
    logger.debug(f"h_check endpoint was reached")
    # return bottle.HTTPResponse(result, status=200, headers=headers)
    return json.loads(result)

@app.route("/metrics", methods=['POST', 'GET'])
def metrics():
    response = {}
    headers = {'Content-type': 'application/json'}
    response['status'] = "Success"
    response['message'] = {'data': {'UserCount': 140, 'UserCountActive': 23}}
    result = json.dumps(response)
    logger.info(f"metrics endpoint was reached")
    # return bottle.HTTPResponse(result, status=200, headers=headers)
    return json.loads(result)


if __name__ == "__main__":
    logger.debug("started the service")
    app.run(host='0.0.0.0',port=7000, debug=True, threaded=True)
