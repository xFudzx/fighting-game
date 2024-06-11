import pygame
from brawlers import fighter
pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting game")

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)

#fighter variables
Gon_size = 50
Gon_scale = 5
Gon_offset = [15, 11]
Gon_data = [Gon_size, Gon_scale, Gon_offset]
Gohan_size = 250
Gohan_scale = 3
Gohan_offset = [112, 107]
Gohan_data = [Gohan_size, Gohan_scale, Gohan_offset]
#load background image
back = pygame.image.load("assets/images/background/bg2.jpg").convert_alpha()

# load sprite sheet
Gon_sheet = pygame.image.load("assets/images/character 1/sprites/Dog-0.png").convert_alpha()
Gohan_sheet = pygame.image.load("assets/images/character2/sprites/wizard.png").convert_alpha()

# define number of steps in each animation
Gon_animation = [4, 4, 3, 5, 2, 4, 5, 7, 1]
Gohan_animation = [8, 8, 1, 8, 8, 3, 7]
#function for drawing background
def bg():
  sized = pygame.transform.scale(back, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(sized, (0, 0))
  
#funtion for drawing fighter health bars
def health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, SILVER, (x - 5, y - 5, 310, 60))
  pygame.draw.rect(screen, RED, (x, y, 300, 50))
  pygame.draw.rect(screen, GREEN, (x, y, 300 * ratio, 50))

character_1 = fighter(200,320, False, Gon_data, Gon_sheet, Gon_animation,)
character_2 = fighter(700,320, True, Gohan_data, Gohan_sheet, Gohan_animation,)

#game loop
game = True
while game:

  clock.tick(FPS)
	
  bg()

  #player stats
  health_bar(character_1.health, 10, 15)
  health_bar(character_2.health, 690, 15)
  

  character_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, character_2)

  character_1.timee()
  character_2.timee()
  pygame.display.flip
  
  character_1.draw(screen)
  character_2.draw(screen)
  pygame.display.flip()


#closes the game and stops the loop using an event
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game = False

  pygame.display.update

#closes pygame
pygame.quit()
