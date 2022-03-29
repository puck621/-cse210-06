from game.scripting.action import Action
from game.shared.point import Point

class ResetActors(Action):
# Implement MoveActorsAction class here! 

    # Override the execute(cast, script) method as follows:
    def execute(self, cast):
        """Executes the reset actors action.

        Args:
        cast (Cast): The cast of Actors in the game.
        script (Script): The script of Actions in the game.
        """
        paddle1 = cast.get_actors("paddle1")
        paddle2 = cast.get_actors("paddle2")
        ball = cast.get_actors("ball")

        paddle1[0].set_position(Point(20, 260))
        paddle2[0].set_position(Point(880,260))
        ball[0].set_position(Point(430, 280))
        



