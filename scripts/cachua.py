#!/usr/bin/env python3

# An interval countdown timer

import time
from playsound import playsound

counter = 3
beep_sec = '/home/hien/OneDrive-HSJ/Workspace/cachua/assets/Electronic_Chime-KevanGC-495939803.mp3'
beep_end = '/home/hien/OneDrive-HSJ/Workspace/cachua/assets/Bicycle Bell Ringing-SoundBible.com-607558103.mp3'

while counter > 0:
    print(counter)
    counter -= 1
    time.sleep(1)
    
playsound(beep)

if __name__=="__main__":
    pass
    
# TODO: add curses
# TODO; read from configuration file

