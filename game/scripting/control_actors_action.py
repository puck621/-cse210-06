import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._direction_2 = Point(-constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
      
        """Moves paddle 1 up"""
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        """Moves paddle 1 down"""
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        paddle1 = cast.get_first_actor("paddle1")
        paddle1.turn_head(self._direction)

        """Moves paddle 2 up"""
        if self._keyboard_service.is_key_down('i'):
            self._direction_2 = Point(0, -constants.CELL_SIZE)

        """Moves paddle 2 down"""
        if self._keyboard_service.is_key_down('k'):
            self._direction_2 = Point(0, constants.CELL_SIZE)

        paddle2 = cast.get_first_actor("paddle2")
        paddle2.turn_head(self._direction_2)
