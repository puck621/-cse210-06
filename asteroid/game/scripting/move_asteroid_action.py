from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveAsteroidAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        asteroids = cast.get_actors(ASTEROIDS_GROUP)

        for asteroid in asteroids:
          body = asteroid.get_body()
          position = body.get_position()
          velocity = body.get_velocity()
          position = position.add(velocity)

          x = position.get_x()
          y = position.get_y()

          if x < 0:
            position = Point(SCREEN_WIDTH - ASTEROIDS_WIDTH, position.get_y())
          elif x > (SCREEN_WIDTH - ASTEROIDS_WIDTH):
            position = Point(0, position.get_y())

          if y < 0:
            position = Point(position.get_x(), SCREEN_HEIGHT - ASTEROIDS_HEIGHT)
          elif y > (SCREEN_HEIGHT - ASTEROIDS_HEIGHT):
            position = Point(position.get_x(), 0)

          body.set_position(position)
