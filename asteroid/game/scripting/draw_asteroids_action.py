from constants import *
from game.scripting.action import Action


class DrawasteroidsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        asteroids = cast.get_actors(ASTEROIDS_GROUP)
        
        for asteroid in asteroids:
            body = asteroid.get_body()

            if asteroid.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            animation = asteroid.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)