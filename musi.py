import numpy as np
from scipy.io.wavfile import write

samplerate = 44100 #Frequecy in Hz


def get_wave(freq, duration=0.28):
    """
    Function takes the "frequecy" and "time_duration" for a wave
    as the input and returns a "numpy array" of values at all points
    in time
    """
    if freq == 0.0:
        duration = 0.25
    amplitude = 4096*2
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)

    return wave


def get_notes():
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B', 'C+', 'c+', 'D+', 'd+', 'E+', 'F+', 'f+', 'G+', 'g+', 'A+', 'a+','B+']
    # base_freq = 261.626 # Frequency of Note C4
    base_freq = 523.251 # Frequency of Note C5
    note_freqs = {octave[i]: base_freq * pow(2, (i / 12)) for i in range(len(octave))}
    note_freqs[''] = 0.0  # silent note
    return note_freqs


def get_song(music_notes):
    note_freqs = get_notes()
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song


#music_notes_v1 = 'G-B-C+---B-C+---B-C+---G-C+-F-----G-B-C+---B-C+---B-C+---G-C+---F-E---F-G---E-D-----C+-B-C+---G-C+-D+-E+---E+-F+-G+---F+-E+-D+-----C+-B-C+---B-C+---G-C+---F-E---F-G---E+-D+-----C+-D+-C+---B-C+---C+-D+-C+---B-C+-----C+-D+-C+---B-C+---D+-E+-F+-G+---F+-E+-C+-D+-----C+-D+-C+---B-C+---C+-D+-C+---B-C+-----C+-D+-C+---B-C+---D+-E+-F+-G+---F+-E+-C+-D+-----C+-B-C+---B-C+---G-C+---F-E---F-G---E-D-----G-B-C+---B-C+---B-C+---G-C+---F-E---F-G---E+-D+-----E+-D+-C+-B-C+---G-C+-D+-E+---G-E+-F+-G+---F+-E+-D+-----C+-D+-C+---B-C+---C+-D+-C+---B-C+-----C+-D+-C+---B-C+---D+-E+-F+-G+---F+-E+-C+-D+-----C+-D+-C+---B-C+---C+-D+-C+---B-C+-----C+-D+-C+---B-C+---D+-E+-F+-G+---F+-E+-C+-D+'
music_notes = 'G-B-C+--B-C+--B-C+--G-C+-F---G-B-C+--B-C+--B-C+--G-C+--F-E--F-G--E-D---C+-B-C+--G-C+-D+-E+--E+-F+-G+--F+-E+-D+---C+-B-C+--B-C+--G-C+--F-E--F-G--E+-D+---C+-D+-C+--B-C+--C+-D+-C+--B-C+---C+-D+-C+--B-C+--D+-E+-F+-G+--F+-E+-C+-D+---C+-D+-C+--B-C+--C+-D+-C+--B-C+---C+-D+-C+--B-C+--D+-E+-F+-G+--F+-E+-C+-D+---C+-B-C+--B-C+--G-C+--F-E--F-G--E-D---G-B-C+--B-C+--B-C+--G-C+--F-E--F-G--E+-D+---E+-D+-C+-B-C+--G-C+-D+-E+--G-E+-F+-G+--F+-E+-D+---C+-D+-C+--B-C+--C+-D+-C+--B-C+---C+-D+-C+--B-C+--D+-E+-F+-G+--F+-E+-C+-D+---C+-D+-C+--B-C+--C+-D+-C+--B-C+---C+-D+-C+--B-C+--D+-E+-F+-G+--F+-E+-C+-D+'
data = get_song(music_notes)
write('river_flows_in_you.wav', samplerate, data.astype(np.int16)) # write in file
print("wrote")