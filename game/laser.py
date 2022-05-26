# points/score and will need key board 
from game.constants import (
    CENTER_X,
    CENTER_Y,
    SHIP_SCALE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WORKING_DIRECTORY,
)

from game.actor import Actor
from game.physics import Physics
import arcade
import math

class Laser(arcade.Sprite):
    def __init__(self, x, y, deltaX, deltaY, rotation): 
        super().__init__(WORKING_DIRECTORY+"\game\images\meteor1.png", SHIP_SCALE)
        self.center_x = SCREEN_WIDTH / 3
        self.center_y = SCREEN_HEIGHT / 3
        self.physics = Physics(x, y, deltaX, deltaY, rotation)
        self.draw()

    # \\\ GET POS ///
    # Returns the current (x, y) coordinates of the ship
    def get_pos(self): return self.physics.get_pos()
    
    def draw(self):
        arcade.draw_line(
            self.center_x, 
            self.center_y, 
            self.center_x - 150 * math.sin(self.physics.get_rotation()),
            self.center_y + 150 * math.cos(self.physics.get_rotation()),
            arcade.color.BLUE,5)

    def update(self):
        self.center_x = self.physics.get_pos()[0]   # set the physics x position over to the sprite's x positon
        self.center_y = self.physics.get_pos()[1]   # set the physics y position over to the sprite's y positon
        self.physics.tick_update()