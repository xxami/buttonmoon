
import pygame
import sys

class Game:
  
  def __init__(self):
    pygame.init()
    pygame.display.set_caption('buttonmoon')
    self.setup()
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      self.render()

  def setup(self):
    self.window = pygame.display.set_mode((1280, 720), 0, 32)
    self.font = pygame.font.SysFont('Arial', 24)

  def render(self):
    self.window.fill((0, 0, 0))
    message = self.font.render('hello, world!', True, (255, 30, 230), (0, 0, 0))
    self.window.blit(message, (0, 0))
    pygame.display.update()

if __name__ == '__main__':
  Game()
