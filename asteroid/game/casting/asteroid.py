from game.casting.actor import Actor


class Asteroid(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, animation, points, debug = False):
        """Constructs a new asteroid.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged.
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points
        self._destroyed = False

    def get_animation(self):
        """Gets the asteroid's image.

        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the asteroid's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the asteroid's points.

        Returns:
            A number representing the asteroid's points.
        """
        return self._points

    def get_destroyed(self):
      return self._destroyed

    def destroy(self):
        self._destroyed = True

