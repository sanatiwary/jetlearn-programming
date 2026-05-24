import pygame
import time

pygame.init()

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('lesson 5')

battler = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L5/imgs/battler.png')
ship = pygame.transform.rotate(pygame.transform.scale(battler, (50, 50)), -90)
shipX = 10
shipY = 400

battler2 = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L5/imgs/battler2.png')
ship2 = pygame.transform.rotate(pygame.transform.scale(battler2, (50, 50)), 90)
ship2X = 940
ship2Y = 400

night = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L5/imgs/night2.png')

border = pygame.Rect(500, 0, 5, 800)

yellowBlt = []
redBlt = []

yellowHlt = 10
redHlt = 10
font = pygame.font.SysFont('Courier', 20)

msg = ""

def handleBlts(yellowBlt, redBlt, yellow, red):
    global redHlt, yellowHlt, msg

    for bullet in yellowBlt:
        pygame.draw.rect(screen, 'yellow', bullet)
        bullet.x += 10

        if bullet.x > 1000:
            yellowBlt.remove(bullet)

        elif bullet.colliderect(red):
            yellowBlt.remove(bullet)
            yellowHlt -= 1

            if yellowHlt <= 0:
                msg = "red has won the game!"

    for bullet in redBlt:
        pygame.draw.rect(screen, 'red', bullet)
        bullet.x -= 10

        if bullet.x < 0:
            redBlt.remove(bullet)
        
        elif bullet.colliderect(yellow):
            redBlt.remove(bullet)
            redHlt -= 1

            if redHlt <= 0:
                msg = "yellow has won the game!"

def drawWinner(msg):
    text = font.render(msg, True, 'white')
    screen.blit(text, (350, 400))

    pygame.display.update()
    pygame.time.delay(5000)

while True:
    screen.blit(night, (0, 0))

    text1 = font.render(f'red health: {redHlt}', True, 'red')
    screen.blit(text1, (10, 10))

    text2 = font.render(f'yellow health: {yellowHlt}', True, 'yellow')
    screen.blit(text2, (780, 10))

    yellow = pygame.Rect(shipX, shipY, 50, 50)
    red = pygame.Rect(ship2X, ship2Y, 50, 50)

    screen.blit(ship, (shipX, shipY))
    screen.blit(ship2, (ship2X, ship2Y))

    pygame.draw.rect(screen, 'white', border)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and shipY > 10:
                shipY -= 10
            
            if event.key == pygame.K_s and shipY < 740:
                shipY += 10

            if event.key == pygame.K_d and shipX < border.x - 50:
                shipX += 10


            if event.key == pygame.K_a and shipX > 10:
                shipX -= 10

            if event.key == pygame.K_UP and ship2Y > 10:
                ship2Y -= 10

            if event.key == pygame.K_DOWN and ship2Y < 740:
                ship2Y += 10

            if event.key == pygame.K_RIGHT and ship2X + 50 < 990:
                ship2X += 10

            if event.key == pygame.K_LEFT and ship2X > border.x:
                ship2X -= 10

            if event.key == pygame.K_LSHIFT and len(yellowBlt) < 3:
                bullet = pygame.Rect(shipX + 50, shipY + 25, 10, 5)

                yellowBlt.append(bullet)

            if event.key == pygame.K_RSHIFT and len(redBlt) < 3:
                bullet = pygame.Rect(ship2X - 50, ship2Y + 25, 10, 5)

                redBlt.append(bullet)

    if redHlt <= 0 or yellowHlt <= 0:
        drawWinner(msg)

        break

    handleBlts(yellowBlt, redBlt, yellow, red)
    pygame.display.update()