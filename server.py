import time
import zmq
import base64

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# ONLY FOR LOCAL SERVER TEST

while True:
    # Wait for next request from client
    message = socket.recv()
    print("Received audio:")

    # Creates a new audio file and writes the message (decoded) from client
    f = open("audio_server.wav", 'wb')
    f.write(base64.b64decode(message))
    print(f)
    f.close()

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send("Successfully sended!")