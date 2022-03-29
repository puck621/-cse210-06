from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Paddle(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self,position, image):
        """Constructs a new Paddle.
        
        Args:Args:
            position: A new instance of Paddle.
            image: a new instance of image
            
        """
        super().__init__(PADDLE,position,Point(0, 0),Point(0, 0))
        # self._body = body
        self._position = position
        self._image = image
        
    def get_body(self):
        """Gets the paddle's body.
        
        Returns:
            An instance of Body.
        """
        return self._body
    def get_image(self):
        """Gets the paddle's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def move_next(self):
        """Moves the paddle using its velocity."""
        position = self.get_position()
        velocity = self.get_velocity()
        new_position = position.add(velocity)
        self.set_position(new_position)

    def move_up(self):
        """Moves the paddle up"""
        
        velocity = Point(-PADDLE_VELOCITY, 0)
        self.set_velocity(velocity)
        
    def move_down(self):
        """Moves the paddle down"""
        
        velocity = Point(PADDLE_VELOCITY, 0)
        self.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the paddle from moving."""
        velocity = Point(0, 0)
        self.set_velocity(velocity)