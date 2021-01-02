#!/bin/python3

import sys, time, math
from synthesizer import Player, Synthesizer, Waveform

pl = Player()
pl.open_stream()

synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
pl.play_wave(synth.generate_constant_wave(0, 1/4))

def get_note (r, n):
    f = r * (2**(n//10) + 2**(n//10) * ((n%10)/10))
    return f

r = 120.0
while (True):
    for n in range(0, 12, 1):
        for n2 in range(12 + 1):
            chord = [get_note(r, n + n2 + n3) for n3 in [0, 3, 7]]
            pl.play_wave(synth.generate_chord(chord, 1/5))

pl.play_wave(synth.generate_constant_wave(0, 1/4))

