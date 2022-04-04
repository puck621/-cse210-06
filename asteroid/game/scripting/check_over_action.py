from constants import *
from game.scripting.action import Action

"""A callback that checks current action and level"""


class CheckOverAction(Action):

    def __init__(self):
        """Sets variables for callback"""
        pass
        
    def execute(self, cast, script, callback):
        """A callback that checks current action and level"""
        asteroids = cast.get_actors(ASTEROIDS_GROUP)
        if len(asteroids) == 0:
            stats = cast.get_first_actor(STATS_GROUP)
            stats.next_level()
            callback.on_next(NEXT_LEVEL)