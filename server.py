#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

import base64

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Wait for next request from client
    message = socket.recv()
    print("Received audio:")

    # Creates a new audio file, 'server_output.wav', and writes the message (decoded) from client
    f = open("server_output.wav", 'wb')
    f.write(message.decode())
    print(f)
    f.close()

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send("Successfully sended!")