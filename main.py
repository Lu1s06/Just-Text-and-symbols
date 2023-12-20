"""game loop and display loop"""
import pynput
from pynput.keyboard import Key

from physics import *

HEIGHT = 150
WIDTH = 200
currently_pressed = []

def on_press(key):

    # print(key, f"{key}", type(key))

    if key not in currently_pressed:
        currently_pressed.append(key)

        if key == Key.esc:
            pass    # TODO add a pause menu
        # display_update()


def on_release(key):
    # ~ currently_pressed[key] = False
    try:
        currently_pressed.remove(key)
    except ValueError:
        pass
    # display_update()

def process_events():
    with pynput.keyboard.Events() as events:
        for event in events:
            if isinstance(event, pynput.keyboard.Events.Release):
                on_release(event.key)
            else:
                on_press(event.key)


def main_game_loop():
    process_events()

if __name__ == "__main__":

    while True:
        main_game_loop()