from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.animation import Animation

class Ship(Actor):
    """A implement used to shoot the Bullet in the game."""

    def __init__(self, body, animation: Animation, debug = False):
        """Constructs a new ship.

        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged.
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the ship's animation.

        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the ship's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the ship using its velocity."""
        print("move next")

        position = self._body.get_position()
        velocity = self._body.get_velocity()

        print("Ship Position %s %s" % (position.get_x(), position.get_y()))
        print("Ship Velocity %s %s" % (velocity.get_x(), velocity.get_y()))

        new_position = position.add(velocity)
        print("New Ship Postion %s %s" % (position.get_x(), position.get_y()))

        self._body.set_position(new_position)

    def move_left(self):
        """Steers the ship to the left."""
        print("Ship Move Left")
        delta = Point(-SHIP_VELOCITY, 0)
        self._body.update_velocity(delta)
        self.move_next()

    def move_right(self):
        """Steers the ship to the right."""
        print("Ship Move Right")
        delta = Point(SHIP_VELOCITY, 0)
        self._body.update_velocity(delta)
        self.move_next()

    def move_up(self):
        """Steers the ship to the left."""
        print("Ship Move Up")
        delta = Point(0, -SHIP_VELOCITY)
        self._body.update_velocity(delta)
        self.move_next()

    def move_down(self):
        """Steers the ship to the right."""
        print("Ship Move Down")
        delta = Point(0, +SHIP_VELOCITY)
        self._body.update_velocity(delta)
        self.move_next()

    def stop_moving(self):
        """Stops the ship from moving."""
        print("Ship Stop")
        velocity = Point(0, 0)
        self._body.set_velocity(delta)
        self.move_next()

