Asteroids
Asteroids is a classic arcade game where a ship shoots increasing number of targets without hitting the targets

Getting Started
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

python3 -m pip install raylib
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

If you are using a Windows device, please replace the text of constants.py with the text from windows_constants.py for proper folder access.

python3 breakdown

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hunter folder and click the "run" icon.
Project Structure
The project files and folders are organized as follows:

root                    (project root folder)
+-- breakdown           (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)

Rules
Player moved up, down, left, and right using the WASD keys.
Player shoots bullets up, down, left, and right using the IJKL keys.
Player gains 50 points when an asteroid is hit.
Player looses a life when hit by an asteroid (bullets can hit the player with no effect). 
Player starts with 3 lives.
When all asteroids are destroyed, a new round begins with 1 more asteroid than the previous round.
Game is over when player has no more lives.

Required Technologies
Python 3.8.0
Raylib Python CFFI 3.7

Authors
Kelsey Scott
Lowry Williams
Emmett Hart
Finley Grant Jarvis