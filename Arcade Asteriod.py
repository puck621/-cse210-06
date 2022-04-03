import arcade
import random
import math
from abc import ABC
from abc import abstractmethod

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

MAX_SPEED = 10

BABY_SHIP_RADIUS = 10
BABY_SHIP_TURN_AMOUNT = 2.9
BABY_SHIP_THRUST_AMOUNT = 0.24
BABY_SHIP_DISTANCE = 2

ALPHA = 250

def draw_new_asteroid(new, old, dx, dy):
    #Defines new asteroid center and velocity after asteroid is hit
    new.center.x = old.center.x
    new.center.y = old.center.y
    new.velocity.dx = old.velocity.dx + dx
    new.velocity.dy = old.velocity.dy + dy
    return new

class Point:
    #Defines item location, default start at center of screen
    def __init__(self):
        self.x = 0
        self.y = 0

class Velocity:
    #Defines item velocity, default is 0
    def __init__(self):
        self.dx = 0
        self.dy = 0

class Flying_Object(ABC):
    #Defines velocity, center, and off screen for all moving objects
    def __init__(self):
        self.center =  Point()
        self.velocity = Velocity()
        self.rotation_speed = 0
        self.rotation_angle = 0

    def advance(self):
    #Defines movement and rotation to be completed each second
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        self.rotation_angle += self.rotation_speed
        if self.rotation_angle == 360:
            self.rotation_angle = 0
        
    @abstractmethod    
    def draw(self):
    #Abstract method for drawing all moving objects in game
        pass
  
    def wrap_screen(self):
    #Tells the program to have all items wrap around the screen when they go over the edge
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = SCREEN_WIDTH
        elif self.center.y > SCREEN_HEIGHT:
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = SCREEN_HEIGHT
           
class Bullet(Flying_Object):
    """Pressing space bar will shoot a bullet.
Bullets are should start with the same velocity of the ship (speed and direction) plus 10 pixels per frame in the direction the ship is pointed. This means if the ship is traveling straight up, but pointed directly to the right, the bullet will have a velocity that is at an angle up and to the right (starting with an upward velocity from the ship, and adding to it a velocity to the right because of the direction the ship is pointed).
There is no limit to the number of bullets that can be fired.
Bullets only live for 60 frames, after which they should "die" and be removed from the game.
For collision detection, you can assume that bullets have a radius of 30"""
    def __init__(self):
        super().__init__()
        self.center =  Point()
        self.velocity = Velocity()
        self.rotation_angle = 0
        self.life = BULLET_LIFE
        self.radius = BULLET_RADIUS
          
    def draw(self):
        #Imports laser image at the angle of the large ship at the center of the large ship
        img = "laserBlue01.png"
        texture = arcade.load_texture(img)
        angle = self.angle
        # Draw bullet
        arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, angle, ALPHA)
        
    def fire(self, bullet_angle, ship_velocity_dx, ship_velocity_dy):
        #Bullets travel at the speed of the ship plus the bullet speed and alive for 60 seconds
        self.velocity.dx = ship_velocity_dx + math.cos(math.radians(bullet_angle)) * BULLET_SPEED
        self.velocity.dy = ship_velocity_dy + math.sin(math.radians(bullet_angle)) * BULLET_SPEED
        self.alive = True     
    
    def advance(self):
        #Move the bullet at current speed, angle, and rotations speed
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        self.rotation_angle += self.rotation_speed
        if self.rotation_angle == 360:
            self.rotation_angle = 0
        
    
class Ship(Flying_Object):
    """The ship obeys the laws of motion. When in motion, the ship will tend to stay in motion.
Note that the angle or orientation of the ship can be different than the direction it is traveling.
The right and left arrows rotate the ship 3 degrees to either direction.
The up arrow will increase the velocity in the direction the ship is pointed by 0.25 pixels/frame.
For collision detection, you can assume the ship is a circle of radius 30."""

    def __init__(self):
        super().__init__()
        self.center =  Point()
        self.velocity = Velocity()
        self.thrust = SHIP_THRUST_AMOUNT
        self.rotation_speed = SHIP_TURN_AMOUNT
        self.rotation_angle = 0
        self.alive = True
        self.center.y = SCREEN_HEIGHT/2 
        self.center.x = SCREEN_WIDTH/2 
        self.velocity.dx = 0
        self.velocity.dy = 0
        self.radius = SHIP_RADIUS
        
    def draw(self):
        #Imports ship art at center of ship with ship radius. Art has to be turned 90 degrees to match code
        img = "playerShip1_orange.png"
        texture = arcade.load_texture(img)
        angle = self.rotation_angle- 90
        arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, angle, ALPHA)
        
    def rotate_left(self):
        #Rotates ship independent of direction or velocity
        self.rotation_angle += self.rotation_speed
        
    def rotate_right(self):
        #Rotates ship independent of direction or velocity
        self.rotation_angle -= self.rotation_speed
         
    def change_velocity_forward(self):
        #Adds velocity at current ship angle.
        #Added a max speed so that the ship did not go out of control for player and wrap screen too fast
        self.velocity.dx += math.cos(math.radians(self.rotation_angle)) * self.thrust
        if self.velocity.dx > MAX_SPEED:
            self.velocity.dx = MAX_SPEED
        self.velocity.dy += math.sin(math.radians(self.rotation_angle)) * self.thrust
        if self.velocity.dy > MAX_SPEED:
            self.velocity.dy = MAX_SPEED
        
    def change_velocity_backward(self):
        #Adds velocity at current ship angle.
        #Added a max speed so that the ship did not go out of control for player and wrap screen too fast
        self.velocity.dx -= math.cos(math.radians(self.rotation_angle)) * self.thrust
        if self.velocity.dx < -MAX_SPEED:
            self.velocity.dx = -MAX_SPEED
        self.velocity.dy -= math.sin(math.radians(self.rotation_angle)) * self.thrust
        if self.velocity.dy < -MAX_SPEED:
            self.velocity.dy = -MAX_SPEED
    
    def advance(self):
        #Move the ship at current speed, angle, and rotations speed
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        if self.rotation_angle == 360:
            self.rotation_angle = 0
            
class Baby_Ship(Flying_Object):

    def __init__(self):
        super().__init__()
        self.center =  Point()
        self.velocity = Velocity()
        self.thrust = BABY_SHIP_THRUST_AMOUNT 
        self.rotation_speed = BABY_SHIP_TURN_AMOUNT
        self.rotation_angle = 0
        self.alive = True
        self.center.y = SCREEN_HEIGHT/2 
        self.center.x = SCREEN_WIDTH/2 - (SHIP_RADIUS * BABY_SHIP_DISTANCE)
        self.velocity.dx = 0
        self.velocity.dy = 0
        self.radius = BABY_SHIP_RADIUS
        
    def draw(self):
        #Imports smaller ship art at center of ship with ship radius. Art has to be turned 90 degrees to match code
        #Spawns relative to the location of the large ship
        img = "playerLife1_orange.png"
        texture = arcade.load_texture(img)
        angle = self.rotation_angle- 90
        arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, angle, ALPHA)
        
    def rotate_left(self):
        #Rotates ship independent of direction or velocity. Small ship has seperate rotation speed
        self.rotation_angle += self.rotation_speed
        
    def rotate_right(self):
        #Rotates ship independent of direction or velocity. Small ship has seperate rotation speed
        self.rotation_angle -= self.rotation_speed
         
    def change_velocity_forward(self):
        #Adds velocity at current ship angle. Small ship has different speed
        #Added a max speed so that the ship did not go out of control for player and wrap screen too 
        self.velocity.dx += math.cos(math.radians(self.rotation_angle)) * self.thrust
        if self.velocity.dx > MAX_SPEED:
            self.velocity.dx = MAX_SPEED
        self.velocity.dy += math.sin(math.radians(self.rotation_angle)) * self.thrust
        if self.velocity.dy > MAX_SPEED:
            self.velocity.dy = MAX_SPEED
        
    def change_velocity_backward(self):
        #Adds velocity at current ship angle. Small ship has different speed
        #Added a max speed so that the ship did not go out of control for player and wrap screen too 
        self.velocity.dx -= math.cos(math.radians(self.rotation_angle)) * self.thrust
        if self.velocity.dx < -MAX_SPEED:
            self.velocity.dx = -MAX_SPEED
        self.velocity.dy -= math.sin(math.radians(self.rotation_angle)) * self.thrust
        if self.velocity.dy < -MAX_SPEED:
            self.velocity.dy = -MAX_SPEED
    
    def advance(self):
        #Move the ship at current speed, angle, and rotations speed
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        if self.rotation_angle == 360:
            self.rotation_angle = 0

class Asteroids(Flying_Object, ABC):
    #Draws asteroids, give it velocity and direction, detects if it goes off screen
    def __init__(self):
        super().__init__()
        self.radius = 0
        self.alive = True
        self.center.x = random.uniform(0,SCREEN_HEIGHT-self.radius)
        self.center.y = random.uniform(0,SCREEN_WIDTH-self.radius)
        self.asteroid_type = 0
          
    @abstractmethod
    def break_apart(self):
        #Abstract for when different asteroids get hit they break into smaller pieces
        pass  


class Small_Asteroids(Asteroids):
    """Rotates at 5 degrees per frame.
For collision detection, can be treated as a circle with radius 2.
If a small asteroid is hit, it is destroyed and removed from the game."""
    def __init__(self):
        super().__init__()
        self.radius = SMALL_ROCK_RADIUS
        self.rotation_speed = SMALL_ROCK_SPIN
        self.rotation_angle = random.uniform(0, 360)
        self.asteroid_type = "small"
        
    def draw(self):
        #Draw small asteroid
        img = "meteorGrey_small1.png"
        texture = arcade.load_texture(img)
        arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, self.rotation_angle, ALPHA) 
     
    def break_apart(self, asteroids):
        #Small asteroid does not break apart, the clean up will delete the sprite from the list
         self.alive = False
         return asteroids 
    
class Medium_Asteroids(Asteroids):
    """Rotates at -2 degrees per frame.
For collision detection, can be treated as a circle with radius 5.
If hit, it breaks apart and becomes two small asteroids.
The small asteroid has the same velocity as the original medium one plus 1.5 pixels/frame up and 1.5 pixels/frame to the right.
The second, 1.5 pixels/frame down and 1.5 to the left."""
    def __init__(self):
        super().__init__()
        self.radius = MEDIUM_ROCK_RADIUS
        self.rotation_speed = MEDIUM_ROCK_SPIN
        self.rotation_angle = random.uniform(0, 360)
        self.asteroid_type = "medium"
        
    def draw(self):
        #Draws asteroid
        img = "meteorGrey_med1.png"
        texture = arcade.load_texture(img)
        arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, self.rotation_angle, ALPHA)
        
    def break_apart(self, asteroids):
        #Breaks apart into 2 small asteroids, the clean up will delete the sprite for the medium asteroid from the list
        small_1 = Small_Asteroids()
        small_1 = draw_new_asteroid(small_1, self, 1.5, 1.5)
        small_2 = Small_Asteroids()
        small_2 = draw_new_asteroid(small_2, self, -1.5, -1.5)
        asteroids.extend([small_1, small_2])
        self.alive = False
        return asteroids
   
class Large_Asteroids(Asteroids):
    """Moves at 1.5 pixels per frame, at a random initial direction.
Rotates at 1 degree per frame.
For collision detection, can be treated as a circle with radius 15.
If a large asteroid gets hit, it breaks apart and becomes two medium asteroids and one small one.
The first medium asteroid has the same velocity as the original large one plus 2 pixel/frame in the up direction.
The second medium asteroid has the same velocity as the original large one plus 2 pixel/frame in the down direction.
The small asteroid has the original velocity plus 5 pixels/frame to the right."""
    def __init__(self):
        super().__init__()
        self.radius = BIG_ROCK_RADIUS
        self.rotation_speed = BIG_ROCK_SPIN
        self.rotation_angle = random.uniform(0, 360)    
        self.velocity.dx = math.cos(math.radians(self.rotation_angle)) * BIG_ROCK_SPEED
        self.velocity.dy = math.sin(math.radians(self.rotation_angle)) * BIG_ROCK_SPEED
        self.asteroid_type = "large"

    def draw(self):
        #Draws asteroid
        img = "meteorGrey_big1.png"
        texture = arcade.load_texture(img)
        arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, self.rotation_angle, ALPHA) 
                                     
    def break_apart(self, asteroids):
        #Breaks apart into 2 medium and 1 small asteroids
        #The clean up will delete the sprite for the medium asteroid from the list
        medium_1 = Medium_Asteroids()
        medium_1 = draw_new_asteroid(medium_1, self, 0, 2)
        medium_2 = Medium_Asteroids()
        medium_2 = draw_new_asteroid(medium_2, self, 0, -2)
        small_1 = Small_Asteroids()
        small_1 = draw_new_asteroid(small_1, self, 5, 0)
        asteroids.extend([medium_1, medium_2, small_1])
        self.alive = False
        return asteroids        
           
class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        self.bullet = Bullet()
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.held_keys = set()
        
        #Sets timers for all text displays for game
        self.round = 1
        self.round_timer = 60
        self.start_time = 100
        self.is_game_over = False

        # TODO: declare anything here you need the game class to track
        self.ship = Ship()
        self.baby_ship = Baby_Ship()
        self.bullets = []
        self.asteroids = []
        
        #Creates original list of asteroids for each round. 
        for i in range(0, (INITIAL_ROCK_COUNT * self.round)):
            large_asteroid = Large_Asteroids()
            self.asteroids.append(large_asteroid)
            
    def draw_score(self):
        """
        Puts the current score on the screen, remains on screen entire game
        """
        score_text = "Round: {}".format(self.round)
        start_x = 10
        start_y = SCREEN_HEIGHT - 30
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=18, color=arcade.color.WHITE)
        
        score_text = "Asteroids Remaining: {}".format(len(self.asteroids))
        start_x = 10
        start_y = SCREEN_HEIGHT - 60
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=18, color=arcade.color.WHITE)
        
    def draw_start(self):
        """
        Draws instructions for the game at beginning of the game, disappears after set amount of time
        """
        if self.start_time > 0:
            score_text = "Protect the Ships. Press SPACE to fire. Press TAB to Stop.".format(self.round)
            start_x = 75
            start_y = SCREEN_HEIGHT - 100
            arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=18, color=arcade.color.WHITE)
    
    def draw_round(self):
        """
        Displays round number in middle of screen at beginning of the round and disappears after a set amount of time.
        The smaller round display is present the whole time
        """
        if self.round_timer > 0:
            score_text = "Round: {}".format(self.round)
            start_x = (SCREEN_WIDTH / 2) -125
            start_y = SCREEN_HEIGHT /2
            arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=50, color=arcade.color.WHITE)
    
    def game_over(self):
        """
        Declares the game over, removes bullets (so ship won't fire), and activates the display for Game Over
        """
        #print ("Game ended. Cleanup")
        for bullet in self.bullets:
            self.bullets.remove(bullet)
        self.is_game_over = True

    def draw_game_over(self):
        #Draw Game Over
        if self.is_game_over:
            #print("Draw Game Over")
            game_text = "Game Over"
            start_x = (SCREEN_WIDTH / 2) - 125
            start_y = SCREEN_HEIGHT / 2
            arcade.draw_text(game_text, start_x=start_x, start_y=start_y, font_size=50, color=arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        
        #Draw all displays for instructions, rounds, and game over text
        self.draw_start()
        self.draw_round()
        self.draw_score()
        self.draw_game_over()
        
        # Drawing asteroids
        for asteroid in self.asteroids:
            asteroid.draw()
            
        #Draw ship
        self.ship.draw()
        self.baby_ship.draw()
                     
        # Drawing bullets
        for bullet in self.bullets:
            bullet.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.start_time -= 1
        self.round_timer -= 1

        # TODO: Tell everything to advance or move forward one step in time
        # Advance asteroids
        for asteroid in self.asteroids:
            asteroid.advance()
            asteroid.wrap_screen()
            
        #Advance ship
        self.ship.advance()
        self.baby_ship.advance()
        self.ship.wrap_screen()
        self.baby_ship.wrap_screen()
                           
        #Advance bullets
        for bullet in self.bullets:
            bullet.advance()
            bullet.wrap_screen()
            bullet.life -= 1
            if bullet.life == 0:
                bullet.alive = False
         
        #After all asteroids are destroyed, a new round starts with more asteroids
        if len(self.asteroids) == 0:
            for i in range(0, (INITIAL_ROCK_COUNT * self.round)):
                large_asteroid = Large_Asteroids()
                self.asteroids.append(large_asteroid)
            self.round += 1
            self.round_timer = 60
        
        # TODO: Check for collisions
        self.check_collisions()           
        
        #Clean up dead sprites for bullets and asteroids
        self.clean_up()

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        The baby ship follows the same key strokes as the large ship but the speed of rotation and thrust are independent.
        Using the same key strokes gives the game play an escort mission quality to add additional strategy for the player.
        Baby ship could move independently using WASD but it proved hard to play and removed the desired escort mission quality. 
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.rotate_left()
            self.baby_ship.rotate_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.rotate_right()
            self.baby_ship.rotate_right()

        if arcade.key.UP in self.held_keys:
            self.ship.change_velocity_forward()
            self.baby_ship.change_velocity_forward()

        if arcade.key.DOWN in self.held_keys:
            self.ship.change_velocity_backward()
            self.baby_ship.change_velocity_backward()
            
        if arcade.key.TAB in self.held_keys:
            self.ship.velocity.dx = 0
            self.ship.velocity.dy = 0
            self.baby_ship.velocity.dx = 0
            self.baby_ship.velocity.dy = 0

        # Machine gun mode, not used because it created too many objects at higher levels
        if arcade.key.SPACE in self.held_keys:
           pass
        
        #Code for moving two ships independently
        """        if arcade.key.LEFT in self.held_keys:
            self.ship.rotate_left()
            
        if arcade.key.RIGHT in self.held_keys:
            self.ship.rotate_right()
            
        if arcade.key.UP in self.held_keys:
            self.ship.change_velocity_forward()
            
        if arcade.key.DOWN in self.held_keys:
            self.ship.change_velocity_backward()
                    
        if arcade.key.A in self.held_keys:
           self.baby_ship.rotate_left()

        if arcade.key.D in self.held_keys:
            self.baby_ship.rotate_right()

        if arcade.key.W in self.held_keys:
            self.baby_ship.change_velocity_forward()

        if arcade.key.S in self.held_keys:
            self.baby_ship.change_velocity_backward()"""



    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                bullet = Bullet()
                bullet.angle = self.ship.rotation_angle 
                bullet_angle = self.ship.rotation_angle 
                bullet.center.x = self.ship.center.x   
                bullet.center.y = self.ship.center.y 
                ship_velocity_dx = self.ship.velocity.dx 
                ship_velocity_dy = self.ship.velocity.dy
                bullet.fire(bullet_angle, ship_velocity_dx, ship_velocity_dy)
                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)
            
    def check_collisions(self):
        #Breaks apart asteroids hit by bullets
        for bullet in self.bullets:
            for asteroid in self.asteroids:
               if bullet.alive and asteroid.alive:
                    collision = bullet.radius + asteroid.radius
                    if (abs(bullet.center.x - asteroid.center.x) < collision and abs(bullet.center.y - asteroid.center.y) < collision):
                        bullet.alive = False
                        asteroid.break_apart(self.asteroids)
                        asteroid.alive = False                   
                        #print("Bullet hit asteroid")
          
        #Ends game if asteroid hits large ship (game end started during clean up)
        for asteroid in self.asteroids:
            if asteroid.alive and self.ship.alive: 
                collision = asteroid.radius + self.ship.radius
                if (abs(self.ship.center.x - asteroid.center.x) < collision and abs(self.ship.center.y - asteroid.center.y) < collision):
                    asteroid.break_apart(self.asteroids)
                    asteroid.alive = False
                    self.ship.alive = False
        
        #Ends game if asteroid hits small ship (game end started during clean up)
        for asteroid in self.asteroids:
            if asteroid.alive and self.baby_ship.alive: 
                collision = asteroid.radius + self.baby_ship.radius
                if (abs(self.baby_ship.center.x - asteroid.center.x) < collision and abs(self.baby_ship.center.y - asteroid.center.y) < collision):
                      self.baby_ship.alive = False
                                    

    def clean_up(self):
        #Ends game if baby ship is hit
        if not self.baby_ship.alive:
           self.game_over()
        
        #Ends game if large ship is hit
        if not self.ship.alive:
           self.game_over()
            
        #Removes bullets that have timed out
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        #Removes asteroids after they have been broken apart
        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)
                
        

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()