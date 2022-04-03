from game.casting.point import Point
from game.casting.rectangle import Rectangle
from constants import SHIP_MAX_VELOCITY

class Body:
    """A rigid body used for physics operations."""

    def __init__(self, position = Point(), size = Point(), velocity = Point()):
        """Constructs a new Body."""
        self._position = position
        self._size = size
        self._velocity = velocity

    def get_position(self):
        """Gets the body's position.

        Returns:
            An instance of Point containing the x and y coordinates.
        """
        return self._position

    def get_size(self):
        """Gets the body's size.

        Returns:
            An instance of Point containing the width and height.
        """
        return self._size

    def get_velocity(self):
        """Gets the body's velocity.

        Returns:
            An instance of Point containing the horizontal and vertical speed.
        """
        return self._velocity

    def get_rectangle(self):
        """Gets the rectangle enclosing the body.

        Returns:
            An instance of Rectangle.
        """
        return Rectangle(self._position, self._size)

    def set_position(self, position):
        """Sets the position to the given value.

        Args:
            position: An instance of Point.
        """
        self._position = position

    def set_size(self, size):
        """Sets the size to the given value.

        Args:
            size: An instance of Point.
        """
        self._size = size

    def set_velocity(self, velocity):
        """Sets the velocity to the given value.

        Args:
            velocity: An instance of Point.
        """
        self._velocity = velocity

    def update_velocity(self, delta):
        """Given a velocity update the current velocty.

        Args:
            velocity: An instance of Point.
        """
        print("Velocity %s %s" % (self._velocity.get_x(), self._velocity.get_y()))
        print("Delta %s %s" % (delta.get_x(), delta.get_y()))
        self._velocity = self._velocity.add(delta)

        if (self._velocity.get_x() > SHIP_MAX_VELOCITY):
          self._velocity = Point(SHIP_MAX_VELOCITY, self._velocity.get_y())
        if (self._velocity.get_x() < -SHIP_MAX_VELOCITY):
          self._velocity = Point(-SHIP_MAX_VELOCITY, self._velocity.get_y())

        if (self._velocity.get_y() > SHIP_MAX_VELOCITY):
          self._velocity = Point(self._velocity.get_x(), SHIP_MAX_VELOCITY)
        if (self._velocity.get_y() < -SHIP_MAX_VELOCITY):
          self._velocity = Point(self._velocity.get_x(), -SHIP_MAX_VELOCITY)

        print("New Velocity %s %s" % (self._velocity.get_x(), self._velocity.get_y()))
