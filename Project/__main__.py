from Event import MouseHandler
from Event import KeyHandler
from WindowManager import Window
import pygame.event
from Project.Scene.TitleScene import GameTitle


WIDTH = 1080
HEIGHT = 720
TITLE = "Optic Engine"

image = None
try:
    image = pygame.image.load("resources/window_icon.png")
except FileNotFoundError as e:
    print("Could not load window icon image")

if image is None:
    exit(1)

screen = Window(WIDTH, HEIGHT, TITLE, image)

screen.add_handler(MouseHandler.on_mouse_down, pygame.MOUSEBUTTONDOWN)
screen.add_handler(MouseHandler.on_mouse_release, pygame.MOUSEBUTTONUP)
screen.add_handler(MouseHandler.on_mouse_move, pygame.MOUSEMOTION)
screen.add_handler(KeyHandler.on_key_click, pygame.KEYDOWN)


screen.current_scene = GameTitle((255, 255, 255), screen)
screen.run()
