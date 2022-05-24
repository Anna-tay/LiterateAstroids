import arcade
import os

WORKING_DIRECTORY = os.getcwd()

# GAME CONSTANTS
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'Literate Astroids'
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
SHIP_SCALE = 1

# SPACESHIP CONSTANTS
SHIP_IDLE = arcade.load_texture(WORKING_DIRECTORY+"\LiterateAstroids\game\images\spaceship.png")