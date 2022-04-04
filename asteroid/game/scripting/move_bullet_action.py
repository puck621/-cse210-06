from constants import *
from game.scripting.action import Action


class MoveBulletAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        """Gets the location and velocity of all bullet actors. Then adds the velocity to the location to create a new location. Reports new location"""
        bullets = cast.get_actors(BULLET_GROUP)

        for bullet in bullets:
          body = bullet.get_body()
          position = body.get_position()
          velocity = body.get_velocity()
          position = position.add(velocity)
          body.set_position(position)
