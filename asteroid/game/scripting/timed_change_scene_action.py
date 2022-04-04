import time
from game.scripting.action import Action


class TimedChangeSceneAction(Action):

    def __init__(self, next_scene, delay):
        """Defines time used for game"""
        self._next_scene = next_scene
        self._delay = delay
        self._start = time.time()
        
    def execute(self, cast, script, callback):
        """Returns the amount of time that has passed since the start of the round"""
        elapsed = time.time() - self._start
        if elapsed >= self._delay:
            callback.on_next(self._next_scene)