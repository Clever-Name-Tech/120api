from flask import Flask, request
import time
import requests
from config import get_posting_url

app = Flask(__name__)


@app.route('/forward', methods=['GET', 'POST'])
def forward_request():
    # Extract parameters from the request if needed
    params = request.json

    posting_url = get_posting_url()

    # Sleep for 120 seconds
    time.sleep(120)

    # Forward the request to the designated URL
    response = requests.post(posting_url, json=params)

    return response.text


@app.route('/forward-url-encoded', methods=['GET', 'POST'])
def forward_request_url_encoded():
    # Extract parameters from the request if needed
    params = request.form

    posting_url = get_posting_url()

    # Sleep for 120 seconds
    time.sleep(120)

    # Forward the request to the designated URL, with URL-encoded parameters
    response = requests.post(posting_url, data=params)

    return response.text


@app.route('/toggle-debug', methods=['GET', 'POST'])
def toggle_debug():
    # Import the current DEBUG value
    try:
        from DEBUG import DEBUG
    except ImportError:
        return "Error reading configuration."

    # Toggle the DEBUG value
    new_debug_value = not DEBUG

    # Update the config.py file
    with open('config.py', 'w') as file:
        file.write(f"DEBUG = {new_debug_value}\n")

    return f"DEBUG set to: {DEBUG}"


@app.route('/update-url', methods=['GET', 'POST'])
def update_url():
    new_url = request.form.get('URL')
    if not new_url:
        return "URL parameter is required.", 400

    # Validate the URL (you may want more robust validation depending on your use case)
    if not new_url.startswith("http://") and not new_url.startswith("https://"):
        return "Invalid URL.", 400

    post_url_path = 'POST_URL.py'

    # Write the new URL value back to the file
    with open(post_url_path, 'w') as file:
        file.write(f"URL = \"{new_url}\"\n")

    return f"POST URL set to: {post_url_path}"


@app.route('/update-testing_url', methods=['GET', 'POST'])
def update_testing_url():
    new_url = request.form.get('URL')
    if not new_url:
        return "URL parameter is required.", 400

    # Validate the URL (you may want more robust validation depending on your use case)
    if not new_url.startswith("http://") and not new_url.startswith("https://"):
        return "Invalid URL.", 400

    post_url_path = 'TEST_URL.py'

    # Write the new URL value back to the file
    with open(post_url_path, 'w') as file:
        file.write(f"URL = \"{new_url}\"\n")

    return f"TEST URL set to: {post_url_path}"


if __name__ == "__main__":
    app.run()
