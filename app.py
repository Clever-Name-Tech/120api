from flask import Flask, request
import time
import requests
import config

app = Flask(__name__)


@app.route('/forward', methods=['POST'])
def forward_request():
    # Extract parameters from the request if needed
    params = request.json

    # Sleep for 120 seconds
    time.sleep(120)

    # Forward the request to the designated URL
    response = requests.post(config.posting_url, json=params)

    return response.text


@app.route('/forward-url-encoded', methods=['POST'])
def forward_request_url_encoded():
    # Extract parameters from the request if needed
    params = request.form

    # Sleep for 120 seconds
    time.sleep(120)

    # Forward the request to the designated URL, with URL-encoded parameters
    response = requests.post(config.posting_url, data=params)

    return response.text


if __name__ == "__main__":
    app.run()
