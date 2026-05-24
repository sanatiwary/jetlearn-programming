import pygame
import time

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("birthday card")

balloon = pygame.image.load("/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L3/imgs/balloon.jpg")
balloonSized = pygame.transform.scale(balloon, (WIDTH, HEIGHT))

cake = pygame.image.load("/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L3/imgs/cake.jpg")
cakeSized = pygame.transform.scale(cake, (100, 100))

gift = pygame.image.load("/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L3/imgs/gift.jpg")
giftSized = pygame.transform.scale(gift, (100, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit() 
                exit(0)

    screen.blit(balloonSized, (0, 0))

    font = pygame.font.SysFont("Times New Roman", 21)
    hpbd = font.render("happy birthday!", True, 'navy')
    screen.blit(hpbd, (200, 200))

    pygame.display.update()
    time.sleep(3)

    wish = font.render("have the best day!", True, 'red')
    screen.blit(wish, (200, 250))
    pygame.display.update()
    time.sleep(3)

    screen.blit(cakeSized, (300, 300))
    pygame.display.update()
    time.sleep(3)

    screen.blit(giftSized, (400, 400))
    pygame.display.update()
    time.sleep(3)
    

    pygame.display.update()

