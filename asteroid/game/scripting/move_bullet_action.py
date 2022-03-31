from constants import *
from game.scripting.action import Action


class MoveBulletAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        bullet = cast.get_first_actor(BULLET_GROUP)
        body = bullet.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
