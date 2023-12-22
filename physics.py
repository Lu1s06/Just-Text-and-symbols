"""
handles most of the calculations in the game

"""

WIDTH = 960
HEIGHT = 290

class BaseSprite():

    """
    adds a base sprite class
    can be referenced in other classes to help implement new sprites
    """
    def __init__(self, x, y, width, height):
        """currently does nothing"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx, dy):
        """
        Move the object by the given amounts in the x and y directions.

        Parameters:
            dx (int): The amount to move in the x direction.
            dy (int): The amount to move in the y direction.
        """

        self.x += dx
        self.y += dy

    def resize(self, dw, dh):
        """
        Resizes the object by adjusting its width and height.

        Parameters:
            dw (int): The amount to increase the width of the object by.
            dh (int): The amount to increase the height of the object by.
        """

        self.width += dw
        self.height += dh
        
class Player(BaseSprite):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
    
    