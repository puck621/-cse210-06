import random
from constants import *
from game.casting.actor import Actor
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point


class Bullet(Actor):
    """A solid, spherical object that is bounced around in the game."""

    def __init__(self, x, y, debug = False):
        """Constructs a new Bullet.

        Args:
            x: Initial X position.
            y: Initial Y Position.
            debug: If it is being debugged.
        """
        super().__init__(debug)

        position = Point(x + SHIP_WIDTH / 2 - BULLET_WIDTH / 2,
            y + SHIP_HEIGHT / 2 + BULLET_WIDTH / 2)
        size = Point(BULLET_WIDTH, BULLET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BULLET_IMAGE)

        self._body = body
        self._image = image
        self._destroyed = False

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

    def get_destroyed(self):
        return self._destroyed

    def destroy(self):
        self._destroyed = True

    def release(self):
        pass

    def release_up(self):
        """Release the Bullet in up."""
        velocity = Point(0, -BULLET_VELOCITY)
        self._body.set_velocity(velocity)

    def release_down(self):
        """Release the Bullet in down."""
        velocity = Point(0, BULLET_VELOCITY)
        self._body.set_velocity(velocity)

    def release_left(self):
        """Release the Bullet in left."""
        velocity = Point(-BULLET_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def release_right(self):
        """Release the Bullet in up."""
        velocity = Point(BULLET_VELOCITY, 0)
        self._body.set_velocity(velocity)
