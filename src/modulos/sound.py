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


    def play(self, x, y) -> NoneType:
        if (y == 0):    return

        for _ in range(344):
            self.stream.write(
                np.sin( 
                    (x % 5) * ( (2 * np.pi) / 5) / y, 
                    dtype=np.float32
                ).tobytes()
            )


    def close(self):
        self.stream.close()
        self.pa.terminate()
