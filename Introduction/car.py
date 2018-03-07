class Car:

    def __init__(self, image=None, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image
        self.x_change = 0
        self.y_change = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def set_x_y(self, x, y):
        self.x = x
        self.y = y

    def move_left(self):
        self.x_change -= 5

    def move_right(self):
        self.x_change -= -5

    def move_up(self):
        self.y_change -= -5

    def move_down(self):
        self.y_change -= 5
