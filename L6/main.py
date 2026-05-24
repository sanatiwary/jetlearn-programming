import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('lesson 6')

bg = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L6/imgs/night2 copy.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('/Users/sana/Desktop/vsc/jetlearn/game dev2 course/L6/imgs/rocket copy.png')

        self.rect = self.image.get_rect()

    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.move_ip(0, -5)

        if keys[pygame.K_a]:
            self.rect.move_ip(-5, 0)

        if keys[pygame.K_s]:
            self.rect.move_ip(0, 5)

        if keys[pygame.K_d]:
            self.rect.move_ip(5, 0)

rocket = Player()
grp1 = pygame.sprite.Group()
grp1.add(rocket)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg, (0, 0))

    keys = pygame.key.get_pressed()
    rocket.update(keys)

    grp1.draw(screen)

    pygame.display.update()
