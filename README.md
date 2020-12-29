# Audio recorder

Record audio with ```pyaudio``` on a Raspberry Pi (with ```ReSpeaker 4-Mic Array```) and send the created wav-file to a server using ```ZMQ```

## Installation

```$ git clone https://github.com/belismau/audio-recorder```

```$ cd audio-recorder```

```$ sudo pip install keyboard```

```$ sudo apt-get install python-pyaudio```

## Run

```$ sudo python app.py```

**Note:** When starting recording, debug messages will pop up. Simply, ignore them. Also, use a keyboard that is plugged into your Raspberry. Otherwise it won't detect keyboard inputs.
