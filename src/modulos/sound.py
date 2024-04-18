import pyaudio
import numpy as np 
from types import NoneType

class Sound(object):

    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(
            format      = pyaudio.paFloat32,
            channels    = 1,
            rate        = 44100,
            output      = True
        )


    def play(self, x=0, y=1.0) -> NoneType:
        if (y == 0):    return

        self.stream.write(
            np.sin( 
                (x % 10) * ( (2 * np.pi) / 10) / y, 
                dtype=np.float32
            ).tobytes()
        )


    def close(self):
        self.stream.close()
        self.pa.terminate()
