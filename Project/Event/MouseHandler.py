import pygame.mouse
from pygame import event
from Project.WindowManager import Window
import Project.Event.MouseHandlerConstants as m


def on_mouse_down(e: event, window: Window) -> None:
    m.mouse_down = True
    buttons = pygame.mouse.get_pressed(3)
    m.left_click = buttons[0]
    m.right_click = buttons[2]
    print("right click:", m.right_click)

    window.current_scene.mouse_event_callback(e)


def on_mouse_release(e: event, window: Window) -> None:
    m.dragging = False
    m.mouse_down = False
    buttons = pygame.mouse.get_pressed(3)
    m.left_click = buttons[0]
    m.right_click = buttons[2]

    window.current_scene.mouse_event_callback(e)


def on_mouse_move(e: event, window: Window) -> None:
    pos = pygame.mouse.get_pos()
    m.moved = False
    if pos == m.previous_pos:
        moved = False
    else:
        moved = True

    if m.mouse_down and moved:
        m.dragging = True
    else:
        m.dragging = False

    window.current_scene.mouse_event_callback(e)


