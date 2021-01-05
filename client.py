import zmq
import base64
import json

def send_audio(audio_info):
    context = zmq.Context()

    # Socket to talk to server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")
    socket.send_pyobj(audio_info)

    print("\nSent the audio information to the server.")
    
    # FOR LOCAL SERVER, server.py
    # Get the reply.
    # message = socket.recv()
    # print("\nReceived reply --- " + str(message) + " ---")