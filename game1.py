import pygame, sys
from pygame.locals import *
import random, time
 

pygame.init()
 

FPS = 60
FramePerSec = pygame.time.Clock()
 

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (100, 175, 100)
 

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
 

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)    
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 550)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(10, 0)
 
     
P1 = Player()
E1 = Enemy()
 

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 

while True:
       

    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 2
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    DISPLAYSURF.fill(WHITE)
 
   
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 

    if pygame.sprite.spritecollideany(P1, enemies):
          class fail(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load("youfail.jpg")
                self.rect = self.image.get_rect()
                self.rect.center = (160, 520)
            def move(self):
                pressed_keys = pygame.key.get_pressed()
                 
                if self.rect.left > 0:
                      if pressed_keys[K_LEFT]:
                          self.rect.move_ip(-5, 0)
                if self.rect.right < SCREEN_WIDTH:        
                      if pressed_keys[K_RIGHT]:
                          self.rect.move_ip(5, 0)
               
          pygame.display.update()
          for entity in all_sprites:
                entity.kill()
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)

