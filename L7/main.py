import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('lesson 7')

bg = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L7/imgs/bg.png')

ground = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L7/imgs/grass.png')

reset = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L7/imgs/restart.png')

groundX = 0

flying = False
gameOver = False

pipeGap = 150
pipeFrequency = (1500)
lastPipe = pygame.time.get_ticks() - pipeFrequency
passPipe = False

score = 0
font = pygame.font.SysFont('Courier', 15)


def drawText(font, color, x, y, text):
  disText = font.render(text, True, color)
  screen.blit(disText, (x, y))


def resetGame():
  grp2.empty()

  bird.rect.x = 25
  bird.rect.y = 275
  score = 0
  return score


class Button():

  def __init__(self, x, y, image):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

  def draw(self):
    action = False

    pos = pygame.mouse.get_pos()

    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1:
        action = True

    screen.blit(self.image, (self.rect.x, self.rect.y))

    return action


resetBtn = Button(300, 300, reset)


class Bird(pygame.sprite.Sprite):

  def __init__(self, x, y):
    super().__init__()

    self.images = []
    self.index = 0
    self.counter = 0

    for i in range(1, 4):
      img = pygame.image.load(f'/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L7/imgs/bird{i}.png')

      self.images.append(img)

    self.image = self.images[self.index]
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

    self.velocity = 0
    self.click = False

  def update(self, keys):
    if flying == True:
      self.velocity += 0.5

      if self.velocity > 8:
        self.velocity = 8

      if self.rect.bottom < 575:
        self.rect.y += self.velocity

    if gameOver == False:
      if keys[pygame.K_SPACE] and self.click == False:
        self.click = True
        self.velocity = -5
      else:
        self.click = False
    self.counter += 1

    if self.counter > 5:
      self.counter = 0
      self.index += 1

      if self.index >= len(self.images):
        self.index = 0
    self.image = self.images[self.index]


class Pipe(pygame.sprite.Sprite):

  def __init__(self, x, y, pos):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L7/imgs/pillar.png')

    self.rect = self.image.get_rect()

    if pos == 1:
      self.image = pygame.transform.flip(self.image, False, True)

      self.rect.bottomleft = (x, y - int(pipeGap / 2))
    if pos == -1:
      self.rect.topleft = (x, y + int(pipeGap / 2))

  def update(self):
    self.rect.x -= 3

    if self.rect.x < 0:
      self.kill()


bird = Bird(50, 300)
grp = pygame.sprite.Group()
grp.add(bird)

grp2 = pygame.sprite.Group()

while True:
  screen.blit(bg, (0, 0))

  screen.blit(ground, (groundX, 575))

  grp.draw(screen)
  keys = pygame.key.get_pressed()
  grp.update(keys)

  if len(grp2) > 0:
    if (grp.sprites()[0].rect.left > grp2.sprites()[0].rect.left) and (grp.sprites()[0].rect.right < grp2.sprites()[0].rect.right) and passPipe == False:
      passPipe = True
    elif gameOver == False:
        score += 1
    if passPipe == True:
      if grp.sprites()[0].rect.left > grp2.sprites()[0].rect.right:
        score += 1
        print(score)

        disText = font.render(str(score), True, color)
        screen.blit(disText, (100, 100))

        passPipe = False

    drawText(font, 'black', 25, 25, 'score: ' + str(score))

  if bird.rect.bottom >= 575:
    gameOver = True
    flying = False
  if gameOver == False and flying == True:
    crtTime = pygame.time.get_ticks()

    groundX -= 3
    if abs(groundX) > 30:
      groundX = 0

    if crtTime - lastPipe > pipeFrequency:
      height = random.randint(-100, 100)

      btmPipe = Pipe(600, 300 + height, -1)
      topPipe = Pipe(600, 300 + height, 1)

      grp2.add(btmPipe)
      grp2.add(topPipe)

      lastPipe = crtTime

  grp2.draw(screen)
  grp2.update()

  #if pygame.sprite.groupcollide(grp, grp2, False, False):
    #gameOver = True

  if gameOver == True:
    if resetBtn.draw() == True:
      gameOver = False
      score = resetGame()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    if event.type == pygame.KEYDOWN and flying == False and gameOver == False:
      flying = True

  pygame.display.update()
