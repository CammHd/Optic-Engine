
import pygame.rect

from Project.WindowManager import Window
import pygame.event as py_event
from typing import Tuple
from pygame import Surface
from pygame.sprite import Sprite


class Scene:

    def __init__(self, color: Tuple[int, int, int], window: Window):
        self.background_color = color
        self.window = window
        self.drawing_objects = dict()

    def update(self):
        pass

    def key_event_callback(self, event: py_event):
        pass

    def mouse_event_callback(self, event: py_event):
        pass


class SceneObject:
    static_id = 0

    def __init__(self):
        self.id = self.static_id
        self.static_id = self.static_id + 1
        self.x = 0
        self.y = 0
        self.velocity = (0, 0)

    def draw(self):
        pass


class SceneObjectSprite(SceneObject, Sprite):

    def __init__(self, sprite: Surface, window_screen: Surface, scene: Scene):
        super().__init__()
        self.sprite = sprite
        self.screen = window_screen
        self.scene = scene
        self.scale = 1
        self.angle = 0
        self.size = sprite.get_rect().size
        self.original_sprite_image = sprite

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))

    def set_rotation(self, rotation: int):
        if self.angle == rotation:
            return
        self.angle = rotation  # note that rotation is counter-clockwise
        self.sprite = pygame.transform.rotate(self.original_sprite_image, self.angle)

    def set_scale(self, scale: float):
        self.scale = scale
        self.sprite = self.sprite.convert(self.sprite)
        self.sprite = pygame.transform.scale(self.original_sprite_image, (scale*self.size[0], scale*self.size[1]))


class SceneObjectPrimitive(SceneObject):
    def __init__(self, rect: pygame.rect.Rect, screen: Window.screen, color: Tuple[int, int, int]):
        super().__init__()
        self.rect = rect
        self.screen = screen
        self.color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 1)


class Entity(SceneObjectSprite):

    def __init__(self, sprite: Surface, screen: Surface, scene: Scene):
        super().__init__(sprite, screen, scene)

    def tick(self):
        pass

    def kill(self):
        if self.scene.drawing_objects.__contains__(self.id):
            self.scene.drawing_objects.pop(self.id)
        super().kill()

    def spawn(self):
        self.scene.drawing_objects[id] = self.id
