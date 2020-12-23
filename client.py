#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
import base64

def send_audio(audio_file):
    # Opens the recorded sound, 'output.wav' and encodes it
    f = open(audio_file, 'rb')
    bytes = bytearray(f.read())
    strng = base64.b64encode(bytes)
    
    context = zmq.Context()

    # Socket to talk to server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print("Sending recorded audio to server...")
    socket.send(strng)

    # Get the reply.
    message = socket.recv()
    print("Received reply --- {message} ---")

    f.close()