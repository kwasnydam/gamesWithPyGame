import pygame
import car as bolid
pygame.init()

# Default dimensions
display_width = 800
display_height = 600

# I will use dictionary to store different colors
colors = {'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 255, 255),
          'green': (0, 255, 0), 'blue': (0, 0, 255)}

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('I guess that is a game')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
x = (display_width * 0.45)
y = (display_height * 0.45)

car = bolid.Car(carImg, x, y)


def display_car():
    gameDisplay.blit(car.image, (car.x + car.x_change, car.y + car.y_change))


crashed = False  # state of the game, if we crashed a vehicle it crashes

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car.move_left()
                display_car()
            if event.key == pygame.K_RIGHT:
                car.move_right()
                display_car()
            if event.key == pygame.K_UP:
                car.move_up()
                display_car()
            if event.key == pygame.K_DOWN:
                car.move_down()
                display_car()



    gameDisplay.fill(colors['white'])
    display_car()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()



