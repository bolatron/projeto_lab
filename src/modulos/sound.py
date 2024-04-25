import pyaudio
from synthesizer import Player, Synthesizer, Waveform

import numpy as np 
from types import NoneType

CHORD_FREQUENCIES = [
    32.7,
    36.7,
    41.2,
    43.7,
    49.0,
    55.0,
    61.7
]


class Sound(object):

    def __init__(self):
        self.player = Player()
        self.player.open_stream()

        self.synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.1, use_osc2=False)

    def play(self, x, y, z) -> NoneType:

        player = Player()
        player.open_stream() 
        synthesizer = Synthesizer(osc1_waveform=Waveform.square, osc1_volume=0.1, use_osc2=False)
        chord_mapped = [CHORD_FREQUENCIES[int(x // (100 / 7))] * 2**int(y // (100 / 7))]
        player.play_wave(synthesizer.generate_chord(chord_mapped, abs(z)))
        player._pyaudio.terminate()


    def close(self):
        pass
