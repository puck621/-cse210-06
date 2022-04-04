from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveShipAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        """Gets the location and velocity of the player's ship. Then adds the velocity to the location to create a new location. Reports new location"""
        ship = cast.get_first_actor(SHIP_GROUP)
        body = ship.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        position = position.add(velocity)

        x = position.get_x()
        y = position.get_y()

        if x < 0:
            position = Point(SCREEN_WIDTH - SHIP_WIDTH, position.get_y())
        elif x > (SCREEN_WIDTH - SHIP_WIDTH):
            position = Point(0, position.get_y())

        if y < 0:
            position = Point(position.get_x(), SCREEN_HEIGHT - SHIP_HEIGHT)
        elif y > (SCREEN_HEIGHT - SHIP_HEIGHT):
            position = Point(position.get_x(), 0)

        body.set_position(position)
