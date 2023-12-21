"""game loop and display loop"""
import random
import time
import itertools

import pynput
from pynput.keyboard import Key

import physics


FPS = 60
LOOP_DELTA = 1./FPS

HEIGHT = 150
WIDTH = 200
currently_pressed = []

def on_press(key):

    # print(key, f"{key}", type(key))

    if key not in currently_pressed:
        currently_pressed.append(key)
        # add keybinds and stuff here :3
        if key == Key.esc:
            pass    # TODO add a pause menu


def on_release(key):
    # ~ currently_pressed[key] = False
    try:
        currently_pressed.remove(key)
    except ValueError:
        pass
    # display_update()


def main_game_loop():
    current_time = target_time = time.perf_counter()
    for i in itertools.count():
        #### loop frequency evaluation
        previous_time, current_time = current_time, time.perf_counter()
        time_delta = current_time - previous_time
        print(f'loop #{i} frequency: {1. / time_delta}')
        #### processing
        # processing example that sleeps a random time between 0 and LOOP_DELTA/2.
        time.sleep(random.uniform(0, LOOP_DELTA / 2.))

        #### sleep management
        target_time += LOOP_DELTA
        sleep_time = target_time - time.perf_counter()
        if sleep_time > 0:
            time.sleep(sleep_time)
        else:
            print('took too long')

if __name__ == "__main__":


    listener = pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

    listener.start()

    while True:
        main_game_loop()
