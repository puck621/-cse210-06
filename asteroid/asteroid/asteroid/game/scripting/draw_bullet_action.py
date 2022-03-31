from constants import *
from game.scripting.action import Action


class DrawBulletAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        bullet = cast.get_first_actor(BULLET_GROUP)
        body = bullet.get_body()

        if bullet.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = bullet.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)