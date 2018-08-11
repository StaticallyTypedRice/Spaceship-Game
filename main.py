import pygame, sys, time

pygame.init()
clock = pygame.time.Clock()

# Colours:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)


WIDTH = 1000
HEIGHT = 600
FPS = 60
pygame.display.set_caption('Spaceship Game')

background = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

spaceship_width = 50
spaceship_height = 50
spaceship_speed = 5

loadSpaceShip = pygame.image.load('spaceshiptriangle.png')
spaceShip = pygame.transform.scale(loadSpaceShip, (spaceship_width, spaceship_height))

def main():
    x_start = (WIDTH * 0.5) - spaceship_width / 2
    y_start = HEIGHT * 3/4

    x = x_start
    y = y_start

    x_change = 0
    y_change = 0

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change += spaceship_speed
                elif event.key == pygame.K_LEFT:
                    x_change += -spaceship_speed
                elif event.key == pygame.K_UP:
                    y_change += -spaceship_speed
                elif event.key == pygame.K_DOWN:
                    y_change += spaceship_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_change += -spaceship_speed
                elif event.key == pygame.K_LEFT:
                    x_change += spaceship_speed
                elif event.key == pygame.K_UP:
                    y_change += spaceship_speed
                elif event.key == pygame.K_DOWN:
                    y_change += -spaceship_speed

        x += x_change
        y += y_change

        background.fill(WHITE)
        changeImg(x, y)

        pygame.display.update()
        clock.tick(FPS)

def getBackground():
    backgroundImg = pygame.image.load('clouds.jpg')
    rect = backgroundImg.get_rect()
    rect.left, rect.top = (0, 0)
    background.blit(backgroundImg, rect)

def changeImg(x, y):
    background.blit(spaceShip, (x, y))

main()


