import pygame
import random

pygame.init()

WIDTH = 640
HEIGHT = 360

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('lesson 7 hw')

bg = pygame.image.load('imgs/bg.png')
bgSized = pygame.transform.scale(bg, (WIDTH, HEIGHT))

ground = pygame.image.load('imgs/grass.png')
groundSized = pygame.transform.scale(ground, (675, 100))

groundX = 0

running = False
gameOver = False

count = 0
clock = pygame.time.Clock()


class Sprite(pygame.sprite.Sprite):

  def __init__(self, x, y):
    super().__init__()

    self.images = []
    self.index = 0
    self.counter = 0

    for i in range(1, 5):
      img = pygame.image.load(f'imgs/run{i}.png')

      imgSized = pygame.transform.scale(img, (50, 100))

      self.images.append(imgSized)

    self.image = self.images[self.index]
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

    self.velocity = 0
    self.click = False

  def update(self, keys):
    if running == True:
      self.running += 0.5

      if self.running > 8:
        self.running = 8

      if self.rect.bottom < 575:
        self.rect.y += self.velocity

    if gameOver == False:
      if keys[pygame.K_SPACE] and self.click == False:
        self.click = True
        self.velocity = -7
      else:
        self.click = False
    self.counter += 1

    if self.counter > 5:
      self.counter = 0
      self.index += 1

      if self.index >= len(self.images):
        self.index = 0
    self.image = self.images[self.index]


class Boost(pygame.sprite.Sprite):

  def __init__(self, img):
    super().__init__()

    self.image = pygame.image.load(img)
    self.image = pygame.transform.scale(self.image, (25, 75))

    self.rect = self.image.get_rect()


boostImgs = ['imgs/juicebox.png', 'imgs/speed.webp']

boostGrp = pygame.sprite.Group()

class Rock(pygame.sprite.Sprite):

  def __init__(self, img):
    super().__init__()

    self.image = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L7/hw/imgs/rocks.webp')
    self.image = pygame.transform.scale(self.image, (25, 75))

    self.rect = self.image.get_rect()

rockGrp = pygame.sprite.Group()
"""
for i in range(100):
  boost = Boost(random.choice(boostImgs))
  boost.rect.x = random.randrange(100, WIDTH)
  boost.rect.y = random.randrange(200, 300)
  boostGrp.add(boost)
"""
#class

sprite = Sprite(50, 310)
grp = pygame.sprite.Group()
grp.add(sprite)

while True:
  clock.tick(60)
  count += 1
  screen.blit(bgSized, (0, 0))

  screen.blit(groundSized, (groundX, 275))
  groundX -= 5
  if count % 100 == 0:
    boost = Boost(random.choice(boostImgs))
    boost.rect.x = random.randrange(100, WIDTH)
    boost.rect.y = random.randrange(200, 300)
    boostGrp.add(boost)

  grp.draw(screen)
  keys = pygame.key.get_pressed()
  grp.update(keys)

  boostGrp.draw(screen)

  if abs(groundX) > 30:
    groundX = 0

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    if event.type == pygame.KEYDOWN and running == False and gameOver == False:
      flying = True

  pygame.display.update()
