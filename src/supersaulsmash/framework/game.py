from collections import defaultdict
import time
import sys

import pygame
from pygame import Rect

from supersaulsmash.framework.helpers import sort_dict, get_matching_objects, Vector, timed
from supersaulsmash.framework.entity import Entity

class Game():
    def __init__(self, fps_cap = 80):

        self.fps_cap = fps_cap
        self.pressed_keys = set()
        self.mouse_down = False
        self.mouse_pos = (0,0)
        self.camera_offset = Vector(0,0)
        self.dt = 0 # Seconds since last tick
        self.last_tick = time.time() # Last time game updated
        self.entities = {}

        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))

    @timed
    def update(self): # Triggers update function for all game objects

        entities = self.get_entities(self.entities) # Get current state entities

        # Calculates the time since the previous tick, allowing for time based physics
        self.dt = round(
            time.time() - self.last_tick, 3
        )

        #print(self.dt)

        for entity in entities:
            #print(entity.active)

            if entity.active: # Only update the entity if its active

                updated_state = entity.update(self.state) # Entity updates might change the game state, so we must update it everytime we run an update

                #print("called")

                self.state = updated_state

            # if self.state != None: # only update the state if we are given a new state
            #     self.state = updated_state
            #
            # elif self.state == None:
            #     print(f"{entity} returned no state! You should really fix that")

        self.last_tick = time.time()

    @timed
    def draw(self):
        # We first sort the game objects by the order in which they need to be drawn

        # The state system is comprised of keys with values
        # Values can also be dicts containing more keys and values

        # Basically extracts all the drawable values from the gamestate and sorts them the order in which they will be drawn
        start_time = time.time()

        layer_dict = self.create_layer_dict(self.state)

        sorted_layers = sort_dict(layer_dict) # THIS MIGHT CAUSE LAG POTENTIALLY no it wont dont be silly

        start_time = time.time()

        # fill screen with black so that if no background is supplied, we dont get ghosts
        self.screen.fill((0,0,0))

        for layer_list in sorted_layers.values():
            for entity in layer_list:
                # retrieve camera offset
                camera_offset = self.camera_offset

                # calculate rect after camera offset
                rect_offset = entity.rect.move(camera_offset)

                # draw the sprite onto the screen using the position of the rect
                self.screen.blit(entity.sprite, rect_offset)

        elapsed_time = time.time() - start_time

        pygame.display.update()

        return elapsed_time # Time it took to draw this frame

    # Extracts all game objects from state dictionary
    def get_entities(self, collection): # Collection can be list or dict

        # I'm keeping this in here for now as it makes it more clear what we are doing
        entities = get_matching_objects(collection, Entity)

        return entities

    def create_layer_dict(self, collection): # Creates a dict of lists where each layer is a list of objects draw on that layer
        layer_dict = defaultdict(list) # Dict of layer lists

        entities = self.get_entities(collection)

        for entity in entities:
            if entity.visible != False:
                layer_dict[entity.layer].append(entity)
        # for key, value in dictionary.items():
        #     if is_instance_or_subclass(value, Entity): # Check if its something we can draw
        #
        #         if value.visible == True:
        #             # Record its layer value
        #             layer_dict[value.layer].append(value)
        #
        #     elif value.__class__ == dict: # If there happens to be ANOTHER dict of values, we dig through it searching for drawable values
        #         # This will return a dict of lists that we will merge with our current dict
        #         new_layer_dict = self.create_layer_dict(value) # AHHH RECURSIONNNN
        #
        #         #print(dict(new_layer_dict))
        #
        #         # Merge layer lists with
        #         for layer_id, layer_list in new_layer_dict.items():
        #             layer_dict[layer_id] += layer_list

        return layer_dict

    def run(self): # Wrapper for running the game
        clock = pygame.time.Clock()

        frames = 0

        while True:

            # We could theoretically have key handling done with an entity
            events = pygame.event.get()

            for event in events:
                match event.type:
                    case pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    case pygame.KEYDOWN:

                        self.state["pressed_keys"].add(event.key)

                    case pygame.KEYUP:

                        self.state["pressed_keys"].remove(event.key)

                    case pygame.MOUSEBUTTONDOWN:

                        self.state["mouse_down"] = True

                    case pygame.MOUSEBUTTONUP:

                        self.state["mouse_down"] = False

                    case pygame.MOUSEMOTION:

                        self.state["mouse_pos"] = event.dict["pos"]


            self.update()
            self.draw()

            frames += 1

            clock.tick(self.fps_cap)
