import pygame
import car as bolid
import time
import obstacle as thing
import random
from enum import Enum


class Speed(Enum):
    SLOW = 2
    MEDIUM = 5
    FAST = 10


class Game:
    """Sets up and runs the game"""
    colors = {'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 255, 255),
              'green': (0, 255, 0), 'blue': (0, 0, 255)}
    carImg = pygame.image.load('racecar.png')
    messages = {'crash_message': 'YOU CRASHED'}
    speed = Speed

    def __init__(self, display_width=800, display_height=600):
        """initializes the game and sets the display parameters"""
        pygame.init()
        self.gameDisplay = None
        self.car = None
        self.gameExit = False
        self.display_width = display_width
        self.display_height = display_height
        self.count = 0
        self.diff = Game.speed.SLOW.value


    @property
    def display_width(self):
        return self.__display_width

    @display_width.setter
    def display_width(self, width):
        #if width != self.display_width:
        self.__display_width = width
        self.update_display()
        #else:
        #    pass

    @property
    def display_height(self):
        return self.__display_height

    @display_height.setter
    def display_height(self, height):
        #if height != self.display_height:
        self.__display_height = height
        self.update_display()
        #else:
        #    pass

    def setUp(self):
        self.gameDisplay = pygame.display.set_mode(
            (self.display_width, self.display_height)
        )
        pygame.display.set_caption('I guess that is a game')
        self.clock = pygame.time.Clock()
        x = (self.display_width * 0.45)
        y = (self.display_height * 0.8)
        self.car = bolid.Car(Game.carImg, x, y)
        self.obstacle = self.generate_obstacle()
        pygame.key.set_repeat(int(1000/60), int(1000/60))

    def generate_obstacle(self):
        obstacle = thing.Obstacle(50, 50, random.randrange(0, self.display_width), 0, Game.colors['black'])
        return obstacle

    def update_display(self, _text=None, _rect=None):
        if self.gameDisplay is not None:
            self.gameDisplay.fill(Game.colors['white'])
            if _text is not None and _rect is not None:
                self.gameDisplay.blit(_text, _rect)
            if self.car is not None:
                self.gameDisplay.blit(self.car.image, (self.car.x + self.car.x_change,
                                                       self.car.y + self.car.y_change))
            pygame.draw.rect(self.gameDisplay, self.obstacle.color, [self.obstacle.x, self.obstacle.y,
                                                                     self.obstacle.width, self.obstacle.height])
            pygame.display.update()

    def crashed(self):
        _car_coordinate = self.car.x + self.car.x_change
        #print(str(_car_coordinate) + " " + str(self.obstacle.y))
        if (_car_coordinate < 0) or (_car_coordinate > (self.display_width - 73)):
            return True

        if self.car.y < self.obstacle.y + self.obstacle.height:
            print(str(self.car.y) + " " + str(self.obstacle.y))
            #print(str(_car_coordinate) + " " + str(self.obstacle.y))
            if ((_car_coordinate < self.obstacle.x + self.obstacle.width)
                    and (_car_coordinate + 73) > (self.obstacle.x)):
                #self.print_message("YOU CRASHED")
                return True
            else:
                pass
        return False

    def print_message(self, message, type=0):
        if type == 0:
            font = pygame.font.Font('freesansbold.ttf', 90)
            TextSurf, TextRect = font.render(message, True, Game.colors['black']), \
                                 font.render(message, True, Game.colors['black']).get_rect()
            TextRect.center = ((self.display_width / 2), (self.display_height / 2))
            #self.gameDisplay.blit(TextSurf, TextRect)
        else:
            font = pygame.font.Font('freesansbold.ttf', 20)
            TextSurf, TextRect = font.render(message, True, Game.colors['black']), \
                                 font.render(message, True, Game.colors['black']).get_rect()
            TextRect.center = ((self.display_width / 10), (self.display_height / 10))

        self.update_display(TextSurf, TextRect)

        time.sleep(2)

    def move_obstacle(self):
        self.obstacle.y += self.diff
        if self.obstacle.y - self.obstacle.height >= self.display_height:
            self.count += 1
            self.obstacle = self.generate_obstacle()
            self.print_message(message='Dodged: ' + str(self.count), type=1)
            return

        #self.update_display()

    def print_score(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('Dodged: ' + str(self.count), True, Game.colors['black'])


    def restore_defaults(self):
        self.car.x_change, self.car.y_change = 0, 0
        self.obstacle = self.generate_obstacle()
        self.count = 0
        self.update_display()

    def run(self):
        while not self.gameExit:
            self.move_obstacle()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
                #print(event)
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        self.car.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.car.move_right()
                    if event.key == pygame.K_UP:
                        self.car.move_up()
                    if event.key == pygame.K_DOWN:
                        self.car.move_down()

            if not self.crashed():
                if self.count > 10:
                    self.diff = Game.speed.MEDIUM.value
                if self.count > 50:
                    self.diff = Game.speed.FAST.value
                self.update_display()
            else:
                self.print_message(Game.messages['crash_message'])
                self.restore_defaults()

            self.clock.tick(60)

        pygame.quit()




