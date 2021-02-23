#!/usr/bin/env python3

from synthesizer import Player, Synthesizer, Waveform

player = Player()
player.open_stream()

synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

player.play_wave(synthesizer.generate_constant_wave(440.0, 1.0))

