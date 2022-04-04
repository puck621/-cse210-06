from constants import *
from game.scripting.action import Action


class DrawAsteroidsAction(Action):

    def __init__(self, video_service):
        """Defines physical queues"""
        self._video_service = video_service

    def execute(self, cast, script, callback):
        """Adds actors to the list of asteroids in ASTEROID_GROUP and puts an image in the location of each actor"""
        asteroids = cast.get_actors(ASTEROIDS_GROUP)

        for asteroid in asteroids:
            body = asteroid.get_body()

            if asteroid.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)

            animation = asteroid.get_animation()
            image = animation.next_image()
            position = body.get_position()
            #print("Asteroid %s %s" % (position.get_x(), position.get_y()))
            self._video_service.draw_image(image, position)