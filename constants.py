from game.shared.color import Color
from game.services.raylib.raylib_physics_service import RaylibPhysicsService

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Pong"
FRAME_RATE = 60
CAPTION = "PONG"
PADDLE = "|\n|\n|"

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
MAX_X = 900
MAX_Y = 600

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
# FONT_FILE = #"batter/assets/fonts/zorque.otf"
# FONT_SMALL = 32
# FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "pong/assets/sounds/boing.wav"
WELCOME_SOUND = "pong/assets/sounds/start.wav"
OVER_SOUND = "pong/assets/sounds/over.wav"

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

# # LEVELS
# LEVEL_FILE = #"batter/assets/data/level-{:03}.txt"
# BASE_LEVELS = 5

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
# STATS_GROUP = "stats"
# DEFAULT_LIVES = 3
# MAXIMUM_LIVES = 5

# HUD
# HUD_MARGIN = 15
# LEVEL_GROUP = "level"
# LIVES_GROUP = "lives"
# SCORE_GROUP = "score"
# LEVEL_FORMAT = "LEVEL: {}"
# LIVES_FORMAT = "LIVES: {}"
# SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "pong/assets/images/ball.png" #"batter/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# PADDLE
PADDLE_GROUP = "paddles"
PADDLE_IMAGES = "pong/assets/images/paddle.png" #[f"pong/assets/images/{n:03}.png" for n in range(100, 103)]
PADDLE_WIDTH = 28
PADDLE_HEIGHT = 81
PADDLE_RATE = 6
PADDLE_VELOCITY = 7
PHYSICS_SERVICE = RaylibPhysicsService()


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"