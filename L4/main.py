import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('Times New Roman', 30)

pygame.display.set_caption('lesson 4')

night = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L4/imgs/night.png')

rocket = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L4/imgs/rocket.png')
rocketX = 100
rocketY = 100

while rocketY < HEIGHT:
    screen.blit(night, (0, 0))
    screen.blit(rocket, (rocketX, rocketY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rocketY -= 10

            if event.key == pygame.K_DOWN:
                rocketY += 10

            if event.key == pygame.K_RIGHT:
                rocketX += 10

            if event.key == pygame.K_LEFT:
                rocketX -= 10

    rocketY += 2
    pygame.display.update()

else:
    screen.blit(night, (0, 0))

    text = font.render('game over!', True, 'honeydew')
    screen.blit(text, (50, 50))

    pygame.display.update()
    time.sleep(2)
    pygame.display.update()