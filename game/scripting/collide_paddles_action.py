from constants import *
from game.scripting.action import Action


class CollidePaddleAction(Action):

    def __init__(self, border_service):
        self._border_service = borders_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor("ball")
        paddle1 = cast.get_first_actor("paddle1")
        paddle2 = cast.get_first_actor("paddle2")

        if self._border_service.has_collided(ball, paddle1):
            ball.bounce_x()

        if self._border_service.has_collided(ball, paddle2):
            ball.bounce_x()
