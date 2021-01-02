#!/bin/python3

import sys, time, math
from synthesizer import Player, Synthesizer, Waveform

pl = Player()
pl.open_stream()

synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
pl.play_wave(synth.generate_constant_wave(0, 1/4))

def get_note (r, n):
    f = r * 2**(n / 12)
    return f

r = 240.0
while (True):
    for n in [0, 0, 2, 3, 1, 4]:
        for n2 in [0, 2, 3, 2, 0, 3]:
            chord = [get_note(r, n + n2 + n3) for n3 in [0, 5]]
            pl.play_wave(synth.generate_chord(chord, 1/6))

pl.play_wave(synth.generate_constant_wave(0, 1/4))

