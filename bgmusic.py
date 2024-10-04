from scamp import *
from scamp_extensions.pitch import Scale
import random
import math


s = Session(tempo=60)

piano = s.new_part("piano")  # s.new_midi_part("midi through 0")

pitches = [60, 62, 64, 67, 69, 72]
pitches = [x + 6 for x in pitches]
initial_pitches = pitches.copy()
scale = Scale.from_pitches(pitches)

skip = 2

# near_even_cycle = [2, 4, 1, 3, 0]

voice_leading_cycle = [2, 4, 1, 3, 0]
next_voice_leading_index = 0

reset_time = 15

def _pedal_change():
    piano.send_midi_cc(64, 0)
    wait(0.05)
    piano.send_midi_cc(64, 1)
    

def degree_to_bump():
    return voice_leading_cycle[next_voice_leading_index]


def next_scale():
    global scale, pitches, next_voice_leading_index
    pitches[degree_to_bump()] += 1
    if degree_to_bump() == 0:
        pitches[-1] += 1
    scale = Scale.from_pitches(pitches)
    next_voice_leading_index = (next_voice_leading_index + 1) % 5


def roll_chord(pitches, volume, dur, spacing=0.08, volume_std=0.2, spacing_std=0.15):
    t_remaining = dur
    for pitch in pitches:
        piano.play_note(pitch, random.gauss(volume, volume * volume_std), t_remaining, blocking=False)
        w = random.gauss(spacing, spacing * spacing_std)
        wait(w)
        t_remaining -= w
    wait_for_children_to_finish()


def modulator():
    global scale, pitches, next_voice_leading_index
    last_time_mod = s.time() % reset_time
    while True:
        fork(_pedal_change)
        chord_pitches = scale[[skip * x for x in range(5) if (skip * x) % 5 != degree_to_bump()]]
        roll_chord(chord_pitches, 0.25, random.choice([3, 5, 7]))
        if s.beat() % reset_time < last_time_mod:
            pitches = initial_pitches.copy()
            next_voice_leading_index = 0
        last_time_mod = s.beat() % reset_time
        next_scale()



def wiggler():
    while True:
        which_degree = [skip * x for x in range(5) if (skip * x) % 5 == degree_to_bump()][0]
        p = scale[which_degree]
        piano.play_note(random.choice([p, p+1]), random.uniform(0.1, 0.2), random.choice([1, 1, 1, 1, 5, 3]) * random.uniform(0.6, 0.65))

        
fork(modulator)
wiggler()
