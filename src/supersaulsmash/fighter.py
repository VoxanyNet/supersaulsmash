from pygame import Rect

from supersaulsmash.framework.entity import Entity
from supersaulsmash.framework.helpers import Vector

class Fighter(Entity):
    def __init__(
        self,
        rect = None,
        velocity = Vector(0,0),
        friction = 0,
        gravity = 0,
        max_velocity = None,
        layer = None,
        sprite_scale_res = None,
        sprite_path = None
    ):

        super().__init__(
            rect,
            velocity,
            friction,
            gravity,
            max_velocity,
            layer,
            sprite_scale_res,
            sprite_path
        )

    def update(self):

        self.move()

        self.apply_friction()

        collisions = self.detect_collisions()
