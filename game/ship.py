# fucnitons 
# - score/points
import arcade
from game.actor import Actor
from game.physics import Physics
from game.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    CENTER_X,
    CENTER_Y,
    SHIP_SCALE,
    WORKING_DIRECTORY,
    )

class Ship(arcade.Sprite):
    def __init__(self): 
        super().__init__(WORKING_DIRECTORY+"\game\images\spaceship.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.physics = Physics(CENTER_X, CENTER_Y, 0, 0, 0) # Insantiate the physics object with POS at the center of the screen
        #self.set_image("images\spaceship.png")
        #self.set_position(640, 360)
    
    # \\\ GET ROTATION ///
    # Returns the current rotation value (in radians) from the physics object in Ship
    def get_rotation(self): return self.physics.get_rotation()

    def draw(self):
        pass

    def update(self):
        """"""