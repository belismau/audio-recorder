import zmq
import base64

def send_audio(audio_file):
    # Opens the recorded sound and encodes it
    f = open(audio_file, 'rb')
    bytes = bytearray(f.read())
    strng = base64.b64encode(bytes)
    f.close()
    
    context = zmq.Context()

    # Socket to talk to server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    socket.send(strng)

    print("\nSent the recorded audio to the server.")
    
    # FOR LOCAL SERVER, server.py
    # Get the reply.
    # message = socket.recv()
    # print("\nReceived reply --- " + str(message) + " ---")