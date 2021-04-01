#!/usr/bin/env python3

# An interval countdown timer

import os
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

    script_path = os.path.abspath(__file__)
    workdir = os.path.dirname(script_path)
    os.chdir(workdir)

    print("Ready, get set,...!")
    for i in range(3):
        playsound('../assets/Electronic_Chime-KevanGC-495939803.mp3')
    print("Go!")
    for exercise in exercises:
        print(exercise + "!")
        count(duration)

    playsound('../assets/Bike Horn-SoundBible.com-602544869.mp3')
