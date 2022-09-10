import pygame
from pygame import Rect

from helpers import Vector
from entity import Entity
from game import Game

# This is an entity that allows the user to manually control the camera with arrow keys
class ManualCamera(Entity): # Should this even be an entity?
    def __init__(self, rect = Rect(0,0,0,0), friction = 0, velocity = Vector(0,0), gravity = 0, max_velocity = None, layer = 0, sprite_scale_res = None, sprite_path = None ):
        super().__init__(rect = rect, layer = layer, sprite_scale_res = sprite_scale_res, sprite_path = sprite_path)

        #self.offset
    def update(self, state):

        state = self.handle_keys(state)

        return state

    def handle_keys(self, state):

        for key in state["pressed_keys"]:
            match key:
                case pygame.K_UP:
                    state["camera_offset"].y += 5
                case pygame.K_DOWN:
                    state["camera_offset"].y -= 5
                case pygame.K_LEFT:
                    state["camera_offset"].x += 5
                case pygame.K_RIGHT:
                    state["camera_offset"].x -= 5

        #print(state["camera_offset"])
        return state

class Background(Entity):
    def __init__(self, rect = None, layer = None, sprite_scale_res = None, sprite_path = None):
        super().__init__(rect = rect, layer = layer, sprite_scale_res = sprite_scale_res, sprite_path = sprite_path)
