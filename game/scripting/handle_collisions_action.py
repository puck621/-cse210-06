import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.reset_set import ResetActors
from game.scripting.reset_point import ResetPoint
from game.casting.score import Score
# from game.scripting.restart_game import execute

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            #self._handle_food_collision(cast)
            # self._handle_grow_tail(cast)
            # self._handle_segment_collision(cast)
            # self._handle_game_over(cast)
            self._out_of_bounds(cast)

    # def _handle_food_collision(self, cast):
    #     """Updates the score nd moves the food if the snake collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     score = cast.get_first_actor("scores")
    #     food = cast.get_first_actor("foods")
    #     snake = cast.get_first_actor("snakes")
    #     snake2 = cast.get_first_actor("snakes2")
    #     head = snake.get_head()
    #     head2 = snake2.get_head()
    #     if head2.get_position().equals(food.get_position()):
    #         points = food.get_points()
    #         snake.grow_tail(1)
    #         score.add_points(points)
    #         food.reset()
    #     if head.get_position().equals(food.get_position()):
    #         points = food.get_points()
    #         snake.grow_tail(1)
    #         score.add_points(points)
    #         food.reset()

        
    
    def _out_of_bounds(self, cast):
        """Add points to the player who scores. Reset the game to initial position if one of the players scores 5 pints 

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        ball = cast.get_first_actor("ball")
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        reset_point = ResetPoint()

        if ball.get_position().get_x() <= 0:
            if score1.get_position().get_x() == 100:
                print("yes")
                score2.add_points()
            elif score1.get_position().get_x() ==550:
                score1.add_points()
            reset_point.right(cast)
            self._winning_set(cast, score1, score2)
            
        elif ball.get_position().get_x()>= 890:    
            if score1.get_position().get_x() == 100:
                score1.add_points()
            elif score1.get_position().get_x() ==550:
                score2.add_points()
            reset_point.left(cast)
            self._winning_set(cast, score1, score2)
            
    
    def _winning_set(self, cast, score1, score2):
        """Checks if one of the players won the set (scores 5 points)

        Args:
            cast (Cast): The cast of Actors in the game.
            score1 (Score): The score of player 1.
            score2 (Score): The score of player 2.
        """
        reset = ResetActors()

        if score1.get_points() == 5: #Lossing the set the players change the side
                score1.reset_score()
                score2.reset_score()
                score1.win_set()
                temp = score1.get_position()
                score1.set_position(score2.get_position())
                score2.set_position(temp)
                score1.update_score()
                score2.update_score()
                reset.execute(cast)
        elif score2.get_points() == 5: #Lossing the set the players change the side
                score1.reset_score()
                score2.reset_score()
                score2.win_set()
                temp = score1.get_position()
                score1.set_position(score2.get_position())
                score2.set_position(temp)
                score1.update_score()
                score2.update_score()
                reset.execute(cast)
             

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # if self._is_game_over:
        #     snake = cast.get_first_actor("snakes")
        #     segments = snake.get_segments()
        #     snake2 = cast.get_first_actor("snakes")
        #     segments2 = snake2.get_segments()
        #     #food = cast.get_first_actor("foods")

        #     x = int(constants.MAX_X / 2)
        #     y = int(constants.MAX_Y / 2)
        #     position = Point(x, y)

        #     message = Actor()
        #     message.set_text("Game Over!")
        #     message.set_position(position)
        #     cast.add_actor("messages", message)

        #     for segment in segments:
        #         segment.set_color(constants.WHITE)
        #     #food.set_color(constants.WHITE)
        #     for segment2 in segments2:
        #         segment2.set_color(constants.WHITE)