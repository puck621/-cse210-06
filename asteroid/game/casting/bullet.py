import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Bullet(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Bullet.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image


    def get_body(self):
        """Gets the Bullet's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the Bullet's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def release_up(self):
        """Release the Bullet in up."""
        velocity = Point(0, BULLET_VELOCITY)
        self._body.set_velocity(velocity)

    def release_down(self):
        """Release the Bullet in down."""
        velocity = Point(0, -BULLET_VELOCITY)
        self._body.set_velocity(velocity)

    def release_left(self):
        """Release the Bullet in left."""
        velocity = Point(-BULLET_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def release_right(self):
        """Release the Bullet in up."""
        velocity = Point(BULLET_VELOCITY, 0)
        self._body.set_velocity(velocity)