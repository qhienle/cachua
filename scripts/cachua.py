#!/usr/bin/env python3

# An interval countdown timer

import time
from playsound import playsound

def count(duration):
    count_beep = '../assets/Electronic_Chime-KevanGC-495939803.mp3'
    final_beep = '../assets/Bicycle Bell Ringing-SoundBible.com-607558103.mp3'

    while duration > 0:
        # TODO: Add curses
        # print(duration)
        # TODO: Play beep in a parallel thread
        # playsound(count_beep)
        duration -= 1
        time.sleep(1)
        
    playsound(final_beep)

if __name__=="__main__":
    # TODO: Read from configuration file
    duration = 15
    exercises = ["Downward Dog", "Cobra", "Side Plank", "Other Side Plank", "Plank", "Plank Again", "Back Stretch"]
    for exercise in exercises:
        print(exercise + "!")
        count(duration)

