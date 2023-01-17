
from Project.Scene.AbstractSceneObjects import Scene
from typing import Tuple
from Project.WindowManager import Window
import pygame
from pygame import event as py_event
from Project.Scene.AbstractSceneObjects import SceneObjectSprite as spriteObject
from Project.Event import MouseHandlerConstants as mouseConstants


class GameTitle(Scene):

    def __init__(self, color: Tuple[int, int, int], window: Window):
        super().__init__(color, window)
        self.start_pos = (0, 0)
        self.finish_transition = False

    def update(self):
        self.window.screen.fill(self.background_color)
        for game_object in self.drawing_objects.values():
            game_object.draw()

    def mouse_event_callback(self, event: py_event):
        rect_id = "rectangle"
        current_pos = pygame.mouse.get_pos()

        image = pygame.image.load("resources/test_square-32x32.png")

        if not self.drawing_objects.__contains__(rect_id):
            self.drawing_objects[rect_id] = spriteObject(image, self.window.screen, self)
        else:
            sprite = self.drawing_objects[rect_id]
            sprite.x = current_pos[0]
            sprite.y = current_pos[1]

        if mouseConstants.left_click:
            self.drawing_objects[rect_id].set_scale(2)

        if mouseConstants.right_click:
            self.drawing_objects[rect_id].set_scale(0.5)








'''
        rect_id = "rectangle"
        display = self.window.screen
        current_pos = pygame.mouse.get_pos()

        if mouseConstants.dragging:
            diffX = current_pos[0]-self.start_pos[0]
            diffY = current_pos[1]-self.start_pos[1]
            rect = pygame.Rect(current_pos[0], current_pos[1], abs(current_pos[0] - self.start_pos[0]),
                               abs(current_pos[1] - self.start_pos[1]))

            if diffX > 0:
                rect.x = self.start_pos[0]
            else:
                rect.x = current_pos[0]

            if diffY > 0:
                rect.y = self.start_pos[1]
            else:
                rect.y = current_pos[1]

            self.drawing_objects[rect_id] = primitiveObject(rect, display, (0, 0, 0))

        else:
            if self.drawing_objects.__contains__(rect_id):
                self.drawing_objects.pop(rect_id)
            self.start_pos = current_pos
'''
