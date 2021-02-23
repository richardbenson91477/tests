#!/usr/bin/env python3

import sys, time, math
from synthesizer import Player, Synthesizer, Waveform

pl = Player()
pl.open_stream()

synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
pl.play_wave(synth.generate_constant_wave(0, 1/4))

scale_n = 7

def get_note (r, n):
    f = r * 2**(n / scale_n)
    return f

r = 120.0
while (True):
    for n2 in range (scale_n + 1):
        for n in range(scale_n + 1):
            chord = [get_note(r, n + n2 + n3) for n3 in [0, 4]]
            pl.play_wave(synth.generate_chord(chord, 1/5))

pl.play_wave(synth.generate_constant_wave(0, 1/4))

