from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, position, name):
        self._name = name
        self._set = 0
        self._text = ""
        self._font_size = 18
        self._color = Color(255, 255, 255)
        self._points = -1
        self.add_points()
        self._position = position
        self._velocity = Point(0, 0)
        
        

    def add_points(self):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += 1
        self.update_score()
        
    def total_points(self):
        return self._points
    
    def win_set(self):
        self._set += 1
        self.update_score()

    def reset_score(self):
        self._points = 0
    
    def get_points(self):
        return self._points

    def update_score(self):
        self.set_text(f"{self._name}: {self._points}       set:{self._set}")
