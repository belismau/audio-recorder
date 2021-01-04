import pyaudio
import keyboard
import wave
from time import time
# from client import send_audio

class Recorder():
    def __init__(self, filename):
        self.audio_format    = pyaudio.paInt16
        self.channels        = 2
        self.sample_rate     = 44100
        self.chunk           = int(0.03*self.sample_rate)
        self.filename        = filename
        self.start           = 's'
        self.quit            = 'q'
    
    def get_index(self):
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
         
        for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                device_name = p.get_device_info_by_host_api_device_index(0, i).get('name')
                if device_name == 'ac108':
                    # Respeaker founded
                    self.respeaker_index = i
                    return
        
        # Runs if respeaker is not found, 
        # on "Built-in Microphone"
        self.respeaker_index = 0

    def record(self):
        self.start_time = time()

        recorded_data = []
        p = pyaudio.PyAudio()

        stream = p.open(format              = self.audio_format, 
                        channels            = self.channels,
                        rate                = self.sample_rate, 
                        input               = True,
                        input_device_index  = self.respeaker_index,
                        frames_per_buffer   = self.chunk)

        print('\nRecording STARTED...')

        while True:
            data = stream.read(self.chunk)
            recorded_data.append(data)

            if keyboard.is_pressed(self.quit) or time() - self.start_time >= 59:
                print('\nRecording STOPPED...')

                # Stop and close the stream
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
recorder.get_index()
recorder.listen()

#...then send to server...
# send_audio(audio_file)