import pygame
from pygame import Surface
from pygame import display
from typing import Callable


class Window:
    screen = None  # static variable
    current_scene = None
    FPS = 60

    def __init__(self, width: int, height: int, title: str, icon: Surface):

        if pygame.get_init():
            raise ValueError("The game is already initialized")

        if not (self.screen is None):
            raise ValueError("the display is already initialized")

        self.running = False
        self.pygame_events = {}  # new dictionary of events to poll
        self.clock = pygame.time.Clock()

        pygame.init()
        if not pygame.get_init():
            raise AssertionError("Could not initialize the game")

        self.screen = display.set_mode((width, height), 0, pygame.OPENGL, 0)
        display.set_caption(title)
        display.set_icon(icon)

    def add_handler(self, handler: Callable, event_type: int):
        self.pygame_events[event_type] = handler

    def poll_events(self):

        for event in pygame.event.get():
            if self.pygame_events.__contains__(event.type):
                self.pygame_events.get(event.type)(event, self)  # call the event handler

            if event.type == pygame.QUIT:
                self.running = False

    def update_scene(self) -> None:
        if self.current_scene is None:
            return

        self.current_scene.update()

    def run(self):
        if self.running:
            return

        self.running = True

        while self.running:
            self.clock.tick(self.FPS)
            self.update_scene()
            self.poll_events()
            display.update()

    pygame.quit()
