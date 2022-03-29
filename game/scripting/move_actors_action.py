from game.scripting.action import Action

class MoveActorsAction(Action):
# Implement MoveActorsAction class here! 

    # Override the execute(cast, script) method as follows:
    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
        cast (Cast): The cast of Actors in the game.
        script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
# 1) get all the actors from the cast
        # actors = cast.get_all_actors()
# 2) loop through the actors
        # for actor in actors:
# 3) call the move_next() method on each actor
                # actor.move_next()
