import board

import simpleio


# Define pin connected to piezo buzzer.
PIEZO_PIN = board.D9

# Define a list of tones/music notes to play.
TONE_FREQ = [
              196,  # G3
              220,  # A4
              247,  # B4
              262,  # C4  # middle C
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A5
              494,  # B5
              523,  # C5
              587,  # D5
              659,  # E5
              698   # F5
            ]

# Main loop will go through each tone in order up and down.
while True:
    # Play tones going from start to end of list.
    for i in range(len(TONE_FREQ)):
        simpleio.tone(PIEZO_PIN, TONE_FREQ[i], duration=0.5)
    # Then play tones going from end to start of list.
    for i in range(len(TONE_FREQ)-1, -1, -1):
        simpleio.tone(PIEZO_PIN, TONE_FREQ[i], duration=0.5)