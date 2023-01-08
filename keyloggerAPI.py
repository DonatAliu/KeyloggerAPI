from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Store the latest key press data in a global variable
latest_key_press = None

@app.route('/key_press', methods=['POST'])
def key_press_post():
    # Get the key press data from the request
    data = request.get_json()
    character = data['character']

    # Update the global variable with the latest key press data
    global latest_key_press
    latest_key_press = character

    # Return a JSON response with the key press data
    return jsonify({'character': character, 'result': 'Success'})

@app.route('/key_press', methods=['GET'])
def key_press_get():
    # Return the latest key press data in the response
    global latest_key_press
    key_press = latest_key_press
    latest_key_press = None
    return jsonify({'character': key_press, 'result': 'Success'})

if __name__ == '__main__':
    app.run()
