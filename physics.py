class BaseSprite():

    """adds a base sprite class
    can be referenced in other classes to help implement new sprites"""
    def __init__(self, x, y, width, height):
        """currently does nothing"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx, dy):
        """moves the sprite by the specified amount"""
        self.x += dx
        self.y += dy

    def resize(self, dw, dh):
        """resizes the sprite by the specified amount"""
        self.width += dw
        self.height += dh
        