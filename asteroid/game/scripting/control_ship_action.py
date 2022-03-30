from constants import *
from game.scripting.action import Action


class ControlshipAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        if self._keyboard_service.is_key_down('a'): 
            ship.move_left()
        if self._keyboard_service.is_key_down('d'): 
            ship.move_right() 
        if self._keyboard_service.is_key_down('w'): 
            ship.move_up()
        if self._keyboard_service.is_key_down('s'): 
            ship.move_down() 
        else: 
            ship.stop_moving()        