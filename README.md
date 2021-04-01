# CàChua

My countdown timer for Pomodoro and Tabata.

## Snippets

Multithreading examples for playing the clock and sound at intervals.

```python
from threading import Thread
from time import sleep
import sys

def timer():
    for i in range(45):
        sleep(1)   #waits 45 seconds
    sys.exit() #stops program after timer runs out, you could also have it print something or keep the user from attempting to answer any longer

def question():
    answer = input("foo?")

t1 = Thread(target=timer)
t2 = Thread(target=question)
t1.start() #Calls first function
t2.start() #Calls second function to run at same time
```

```python
from threading import Thread
from time import sleep

def timer():
    sleep_duration = 10
    while sleep_duration > 0:
        print(f"you have {sleep_duration} seconds left")
        sleep(1)
        sleep_duration -= 1
    print("timer completed")

def main():
    timer_thread = Thread(target=timer)

    timer_thread.start()

    for i in range(0, 15):
        # check the timer
        if not timer_thread.is_alive():
            # timer is complete
            print("oh no. you ran out of time!")
            break
        # game logic here
        print(f"answer question {i}")
        sleep(1)

if __name__ == "__main__":
    main()
```
