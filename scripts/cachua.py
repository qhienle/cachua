#!/usr/bin/env python3

# An interval countdown timer

import os
from time import sleep
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
        sleep(1)

    playsound(final_beep)

def main():

    # Configure exercises
    # TODO: Read from configuration file
    duration = 15
    exercises = ["Downward Dog", "Cobra", "Side Plank", "Other Side Plank", "Plank", "Plank Again", "Back Stretch"]

    # Set workdir to script's dir in order to access assets using relative paths
    script_path = os.path.abspath(__file__)
    workdir = os.path.dirname(script_path)
    os.chdir(workdir)

    # Warn: Ready, get set, go!
    print("Ready, get set,...!")
    for i in range(3):
        playsound('../assets/Electronic_Chime-KevanGC-495939803.mp3')
    print("Go!")

    # Begin series of exercises
    for exercise in exercises:
        print(exercise + "!")
        count(duration)

    playsound('../assets/Bike Horn-SoundBible.com-602544869.mp3')

if __name__=="__main__":
    main()
