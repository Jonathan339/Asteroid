import pygame
from pygame.locals import *
import os
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
DATOS_IMA = 'ima'

def load_image(name, colorkey = False):
   """ Carga una imagen, devuelve una superficie y su rectángulo"""
   
   fullname = os.path.join(DATOS_IMA, name)
   
   try: image = pygame.image.load(fullname)
   except pygame.error, message:
      print 'No se ha podido cargar la imagen', fullname
      raise SystemExit, message
      
   image = image.convert()
   if colorkey:
      colorkey = image.get_at((0,0))
      image.set_colorkey(colorkey, RLEACCEL)
   return image, image.get_rect()
   
class Nave(pygame.sprite.Sprite):
   """ Este objeto representa la nave que controla el jugador"""
   
   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image, self.rect = load_image('nave.gif')
      self.rect.centerx = SCREEN_WIDTH / 2
      self.rect.centery = SCREEN_HEIGHT - 400
      self.speed = [0,0]
      
   def gravedad(self, gravedad):
      self.speed[1] = self.speed[1] + gravedad
      
   def mueve_nave(self):
      tecla = pygame.key.get_pressed()
      
      if tecla[K_UP]:
         self.speed[1] = self.speed[1] - 0.3
         
      if tecla[K_LEFT]:
         self.speed[0] = self.speed[0] - 0.3
         
      if tecla[K_RIGHT]:
         self.speed[0] = self.speed[0] + 0.3
      
   def update(self):
      if self.rect.top <1>= SCREEN_HEIGHT:
         self.rect.bottom = SCREEN_HEIGHT
         self.speed[1] = 0
      if self.rect.left <1>= SCREEN_WIDTH + self.rect.width + 1:
         self.rect.left = -self.rect.width
      self.rect.move_ip((self.speed[0], self.speed[1]))
      
class Meteorito(pygame.sprite.Sprite):
   
   def __init__(self, rock):
      pygame.sprite.Sprite.__init__(self)
      self.image, self.rect = load_image(rock)
      self.rect.centerx = random.randrange(0, SCREEN_WIDTH)
      self.rect.centery = random.randrange(0, SCREEN_HEIGHT)
      self.speed = [random.randrange(1, 3), random.randrange(1, 3)]
      
   def update(self):
      if self.rect.top <1>= SCREEN_HEIGHT + self.rect.height + 1:
         self.rect.top = -self.rect.height
      if self.rect.left <1>= SCREEN_WIDTH + self.rect.width + 1:
         self.rect.left = -self.rect.width
      self.rect.move_ip((self.speed[0], self.speed[1]))
   
# ----------------------------------------------------------------------
   
def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   pygame.display.set_caption('Aterriza la nave')
   icon, icon_rect = load_image('icon.gif')
   pygame.display.set_icon(icon)
   
   background, background_rect = load_image('background.jpg')
   screen.blit(background, (0,0))
   
   nave = Nave()
   meteorito1 = Meteorito('big_rock1.gif')
   todos_sprites = pygame.sprite.RenderPlain((nave, meteorito1))
   clock = pygame.time.Clock()
   
   while True:
      clock.tick(60)
      
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            raise SystemExit
         elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
               raise SystemExit
      
      meteorito1.update()
      nave.mueve_nave()
      nave.gravedad(0.1)
      nave.update()
      
      screen.blit(background, (0,0))
      todos_sprites.draw(screen)
      pygame.display.flip()
   
if __name__ == '__main__':   main()
import os
import pygame

from pygame.locals import *
x = 100
y = 0
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pygame
pygame.init()
screen = pygame.display.set_mode((100,100))

# wait for a while to show the window.
import time
time.sleep(2)