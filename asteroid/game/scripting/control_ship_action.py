from constants import *
from game.casting.bullet import Bullet
from game.scripting.action import Action

class ControlshipAction(Action):

    def __init__(self, keyboard_service):
        """Defines keyboard inputss"""
        self._keyboard_service = keyboard_service

    def _create_bullet(self, ship, cast):
        """Creates new actor Bullet with the trajectory and location of the ship"""
        ship_position = ship.get_body().get_position()
        x = ship_position.get_x()
        y = ship_position.get_y()
        bullet = Bullet(x, y, True)
        cast.add_actor(BULLET_GROUP, bullet)
        return bullet

    def _shoot_up(self, ship, cast):
        """Creates a bullet at the location of the top of the ship with up velocity"""
        bullet = self._create_bullet(ship, cast)
        bullet.release_up()

    def _shoot_left(self, ship, cast):
        """Creates a bullet at the location of the left of the ship with left velocity"""
        bullet = self._create_bullet(ship, cast)
        bullet.release_left()

    def _shoot_down(self, ship, cast):
        """Creates a bullet at the location of the bottom of the ship with downward velocity"""
        bullet = self._create_bullet(ship, cast)
        bullet.release_down()

    def _shoot_right(self, ship, cast):
        """Creates a bullet at the location of the right of the ship with right velocity"""
        bullet = self._create_bullet(ship, cast)
        bullet.release_right()

    def execute(self, cast, script, callback):
        """Registers key strokes, moves the ship, creates correstoponding bullet, and creates text in terminal to track movements for debugging"""
        ship = cast.get_first_actor(SHIP_GROUP)
        if self._keyboard_service.is_key_down('a'):
            print("Control Ship Left")
            ship.move_left()
        if self._keyboard_service.is_key_down('d'):
            print("Control Ship Right")
            ship.move_right()
        if self._keyboard_service.is_key_down('w'):
            print("Control Ship Up")
            ship.move_up()
        if self._keyboard_service.is_key_down('s'):
            print("Control Ship Down")
            ship.move_down()
        if self._keyboard_service.is_key_pressed('i'):
            print("Control Shoot Up")
            self._shoot_up(ship, cast)
        if self._keyboard_service.is_key_pressed('j'):
            print("Control Shoot Left")
            self._shoot_left(ship, cast)
        if self._keyboard_service.is_key_pressed('k'):
            print("Control Shoot Down")
            self._shoot_down(ship, cast)
        if self._keyboard_service.is_key_pressed('l'):
            print("Control Shoot Right")
            self._shoot_right(ship, cast)