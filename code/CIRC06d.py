# CIRC06 Pizeo music
import board
import time
import simpleio

"""
Some external wikipedia reference information
https://en.wikipedia.org/wiki/Piano_key_frequencies
https://en.wikipedia.org/wiki/Octave
https://en.wikipedia.org/wiki/List_of_musical_symbols
"""

# Define pin connected to piezo buzzer.
PIEZO_PIN = board.D9
Measure_time = 2.0      # time in seconds of one musical measure
SONG_SEPARATION = 3.0   # time between songs


TONE_FREQ = {   # use a dictionary to map note names to note frequency
            'REST' : 0,
            'G3' : 196,
            'A4' : 220,
			'B4' : 247,
			'C4' : 262, # middle C
            'D4' : 294,
            'E4' : 330,
            'F4' : 349,
            'G4' : 392,
            'A5' : 440,
            'B5' : 494,
			'C5' : 523,
			'D5' : 587,
            'E5' : 659,
            'F5' : 698
			}
			
# the music is encoded in a list of lists
# the inner list is the note name followed
# by the length of time the note is held as a fraction of the measure time
# So it's 1/4 for quarter notes and 1/2 for half notes
# use 1 for a whole rest.

# the outer list is the notes in the musical score

twinkle = [
           ['C4', 1/4], ['C4', 1/4], ['G4', 1/4], ['G4', 1/4],
           ['A5', 1/4], ['A5', 1/4], ['G4', 1/2], ['F4', 1/4],
           ['F4', 1/4], ['E4', 1/4], ['E4', 1/4], ['D4', 1/4],
           ['D4', 1/4], ['C4', 1/2], ['REST', 1]
          ]

birthday = [
            ['C4', 1/4], ['C4', 1/4], ['D4', 1/4], ['C4', 1/4],
            ['F4', 1/4], ['E4', 1/2],
            ['C4', 1/4], ['C4', 1/4], ['D4', 1/4], ['C4', 1/4],
            ['G4', 1/4], ['F4', 1/2], ['REST', 1]
           ]

joy =   [
          ['E4', 1/4], ['E4', 1/4], ['F4', 1/4], ['G4', 1/4],
          ['G4', 1/4], ['F4', 1/4], ['E4', 1/4], ['D4', 1/4],
          ['C4', 1/4], ['C4', 1/4], ['D4', 1/4], ['E4', 1/4],
          ['E4', 1/4], ['D4', 1/4], ['D4', 1/2],
          ['E4', 1/4], ['E4', 1/4], ['F4', 1/4], ['G4', 1/4],
          ['G4', 1/4], ['F4', 1/4], ['E4', 1/4], ['D4', 1/4],
          ['C4', 1/4], ['C4', 1/4], ['D4', 1/4], ['E4', 1/4],
          ['D4', 1/4], ['C4', 1/4], ['C4', 1/2], ['REST', 1]
        ]
# now we will define a subroutine to play the song
def play_music(song_name):
    for note in song_name:
 #       print (note)
        if (note[0] == 'REST'):
            time.sleep((note[1] * Measure_time ))
        else:
            simpleio.tone(PIEZO_PIN, TONE_FREQ[note[0]], duration= (note[1] * Measure_time ) )

while True:
    play_music(twinkle)
#    time.sleep(SONG_SEPARATION) # some quiet time between songs
    play_music(birthday)
#    time.sleep(SONG_SEPARATION)
    play_music(joy)
#    time.sleep(SONG_SEPARATION)