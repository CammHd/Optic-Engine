import pygame.event as py_event


class KeyboardEvent:
    def __init__(self, event: py_event):
        self.event = event

    def get_event(self) -> py_event:
        return self.event


class MouseEvent:
    def __init__(self, event: py_event):
        self.event = event

    def get_event(self) -> py_event:
        return self.event
