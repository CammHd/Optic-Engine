import pygame
from pygame import event
from pygame.locals import *
from Project.WindowManager import Window

shift_pressed = False
key_hold = False


def on_key_click(e: event, window: Window) -> None:
    window.current_scene.key_event_callback(e)


def on_key_release(e: event, window: Window) -> None:
    window.current_scene.key_event_callback(e)


def on_key_hold(e: event, window: Window) -> None:
    window.current_scene.key_event_callback(e)
