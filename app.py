import pyaudio
import keyboard
import numpy as np
import wave
from scipy.io import wavfile
from client import send_audio

class Recorder():
    def __init__(self, filename):
        self.audio_format   = pyaudio.paInt16
        self.channels       = 2
        self.sample_rate    = 44100
        self.chunk          = int(0.03*self.sample_rate)
        self.filename       = filename
        self.start          = 's'
        self.quit           = 'q'

    def record(self):
        print('\nRecording started...')
        recorded_data = []
        p = pyaudio.PyAudio()

        stream = p.open(format              = self.audio_format, 
                        channels            = self.channels,
                        rate                = self.sample_rate, 
                        input               = True,
                        frames_per_buffer   = self.chunk)
        while True:
            data = stream.read(self.chunk)
            recorded_data.append(data)

            if keyboard.is_pressed(self.quit):
                print('\nRecording stopped...')
                # stop and close the stream
                stream.stop_stream()
                stream.close()
                p.terminate()
                
                wf = wave.open(self.filename, 'wb')
                wf.setnchannels(self.channels)
                wf.setsampwidth(p.get_sample_size(self.audio_format))
                wf.setframerate(self.sample_rate)
                wf.writeframes(b''.join(recorded_data))
                wf.close()

                break

    def listen(self):
        print("Press `" + self.start + "` to start and `" + self.quit + "` to quit!")
        while True:
            if keyboard.is_pressed(self.start):
                self.record()
                break

audio_file = 'audio.wav'
recorder = Recorder(audio_file)
recorder.listen()

#...then send to server...
#send_audio(audio_file)