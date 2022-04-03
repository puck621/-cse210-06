from game.casting.color import Color
# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------
import os
import sys
import random
import math

"""These values are constant throughout the game.  They control the size of the GUI,
the colors used, the speed of the frame rate , the ship size and speed, the bullets size and speed,
and the asteroids size and speed."""

ROOT = os.path.dirname(sys.modules['__main__'].__file__)

# GAME
GAME_NAME = "Asteriods"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = ROOT + "/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = ROOT + "/assets/sounds/boing.wav"
WELCOME_SOUND = ROOT + "/assets/sounds/start.wav"
OVER_SOUND = ROOT + "/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = ROOT + "/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# --------------------------------------------------------------------------------------------------
# SCRIPTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# --------------------------------------------------------------------------------------------------
# CASTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BULLET
BULLET_GROUP = "bullets"
BULLET_IMAGE = ROOT + "/assets/images/000.png"
BULLET_WIDTH = 28
BULLET_HEIGHT = 28
BULLET_VELOCITY = 6
BULLET_LIFE = 60

# SHIP
SHIP_GROUP = "ships"
SHIP_IMAGES =[  ROOT + "/assets/images/001.png" ]
SHIP_WIDTH = 106
SHIP_HEIGHT = 28
SHIP_RATE = 6
SHIP_VELOCITY = 1
SHIP_MAX_VELOCITY = 5
SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25

# ASTEROIDS
ASTEROIDS_GROUP = "asteroids"
INITIAL_ROCK_COUNT = 3
ROCK_COUNT_INCREMENT = 1
ASTEROIDS_IMAGES = {
    "l": [f"{ROOT}/assets/images/{i:03}.png" for i in range(2,40)]
}
ASTEROIDS_DELAY = 0.5
ASTEROIDS_RATE = 4
ASTEROIDS_POINTS = 50
ASTEROIDS_WIDTH =30
ASTEROIDS_HEIGHT =30


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START. USE WASD TO MOVE & IJKL TO FIRE"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"


