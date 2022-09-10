import time

from pygame.math import Vector2

class Vector(Vector2):
    def slow(self, delta_x = 0, delta_y = 0): # Subtracts if positive, adds if negative
        if self.x < 0:
            if self.x + delta_x > 0:
                self.x = 0
            else:
                self.x += delta_x
        elif self.x > 0:
            if self.x - delta_x < 0:
                self.x = 0
            else:
                self.x -= delta_x

        if self.y < 0:
            if self.y + delta_y > 0:
                self.y = 0
            else:
                self.y += delta_y
        elif self.y > 0:
            if self.y - delta_y < 0:
                self.y = 0
            else:
                self.y -= delta_y

def timed(function):

    def timed_function(*args):

        start_time = time.time()

        function(*args)

        elapsed_time = time.time() - start_time

        #print(f"{elapsed_time} to complete.")

    return timed_function



# Extracts all game objects from state dictionary
def get_matching_objects(collection, object_type): # Collection can be list or dict
    entities = [] # All game objects

    if collection.__class__ == dict: # We need to make this check because iterating through a dicts values requires .items()
        for value in collection.values():
            if isinstance(value, object_type): # Check if its something we can draw
                entities.append(value)

            elif value.__class__ == dict or list: # If there happens to be ANOTHER dict of values, we dig through it searching for drawable values
                # This will return a dict of lists that we will merge with our current dict
                new_entities = get_matching_objects(value, object_type) # AHHH RECURSIONNNN

                # Merge layer lists with
                entities += new_entities

    elif collection.__class__ == list:
        for value in collection:
            if isinstance(value, object_type): # Check if its something we can draw
                entities.append(value)

            elif value.__class__ == dict or list: # If there happens to be ANOTHER dict of values, we dig through it searching for drawable values
                # This will return a dict of lists that we will merge with our current dict
                new_entities = self.get_matching_objects(value, object_type) # AHHH RECURSIONNNN

                # Merge layer lists with
                entities += new_entities



    return entities

# def is_instance_or_subclass(object, class_type):

#     # Check if the object is an instance of a game object
#     if object.__class__ is class_type:
#         return True # We also draw base game object

#     # Check if this object's class's parent is Game Object
#     if hasattr(object.__class__, "__bases__") != True: # Check if the value has a parent class
#         return False # If the value does not have a base class, we can assume its not a Game Object

#     # This statement checks if the value is an instance (or instance of a subclass) of GameObject
#     if object.__class__.__bases__[0] is class_type:
#         return True # We don't render values that aren't Game Objects

#     else:
#         return False

def sort_dict(unsorted_dictionary):
    keys = []

    for key in unsorted_dictionary:
        keys.append(key)

    sorted_keys = sorted(keys)

    sorted_dictionary = {}

    for key in sorted_keys:
        sorted_dictionary[key] = unsorted_dictionary[key]

    return sorted_dictionary
