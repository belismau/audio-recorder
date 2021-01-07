import time
import zmq
import base64
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

# ONLY FOR LOCAL SERVER TEST

while True:
    # Wait for next request from client
    message = socket.recv_pyobj()
    print("Received audio:")

    # access: for ex. message['channels']

    time.sleep(1)

    #  Send reply back to client
    socket.send_string("Successfully sended!")