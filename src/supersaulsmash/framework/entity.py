from collections import defaultdict
import time
import sys

import pygame
from pygame import Rect

from supersaulsmash.framework.helpers import sort_dict, get_matching_objects, Vector, timed


class Entity:
    def __init__(self, rect = None, friction = 0, velocity = Vector(0,0), gravity = 0, max_velocity = None, layer = None, sprite_scale_res = None, sprite_path = None):

        # Check for required args
        if rect == None:
            raise TypeError("Missing rectangle argument")
        else:
            self.rect = rect

        if layer == None:
            raise TypeError("Missing layer argument")
        else:
            self.layer = layer

        self.gravity = gravity

        self.velocity = velocity

        self.friction = friction

        self.max_velocity = max_velocity

        self.active = True # We set this value to false when we want to kill the entity

        # Sprite loading
        if sprite_path != None:
            print("Loading sprite")
            self.sprite = pygame.image.load(sprite_path)#.convert()# <-- This screws with PNGs for some reason but has MASSIVE FPS gai

            self.visible = True

        else:
            print(f"No sprite for entity!")
            self.visible = False # Objects that are not visible will not be drawn

        # Sprite scaling
        if sprite_scale_res and sprite_path:
            self.sprite = pygame.transform.scale(self.sprite, sprite_scale_res)

    def detect_collisions(self, collection):

        colliding_entities = [] # all entities that this entity are colliding with

        # fetch all entity objects from given collection
        for entity in get_matching_objects(collection, Entity):

            # check if our entity collides this one
            if self.rect.colliderect(entity.rect):
                colliding_entities.append(entity)

        return colliding_entities

    def move(self, state):

        if self.max_velocity: # only check if specified

            # check if we went above our max velocity
            if self.velocity.x < 0:
                if self.velocity.x < -self.max_velocity.x:
                    self.velocity.x = -self.max_velocity.x
            elif self.velocity.x > 0:
                if self.velocity.x > self.max_velocity.x:
                    self.velocity.x = self.max_velocity.x

            if self.velocity.y < 0:
                if self.velocity.y < -self.max_velocity.y:
                    self.velocity.y = -self.max_velocity.y
            elif self.velocity.y > 0:
                if self.velocity.y > self.max_velocity.y:
                    self.velocity.y = self.max_velocity.y

        # moves the rect by velocity vector
        self.rect.move_ip(self.velocity)

        return state

    def apply_friction(self, state):

        # If moving, we apply friction
        if abs(self.velocity.x) or abs(self.velocity.y) > 0:
            #print("applying friction")
            self.velocity.slow(delta_x = self.friction, delta_y = self.friction)

        return state

    def apply_gravity(self, state):

        self.velocity.y += self.gravity

        return state

    def update(self, state): # the base entity does not do anything when updated

        return state # just return the state as we found it, no harm done
