import pygame
from pygame import mixer
from brawlers import fighter
import pause
 
mixer.init()
pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting game")


clock = pygame.time.Clock()
FPS = 60


RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)

#game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#fighter variables
Gon_size = 36
Gon_scale = 2
Gon_offset = [15, 52]
Gon_data = [Gon_size, Gon_scale, Gon_offset]
Gohan_size = 250
Gohan_scale = 2
Gohan_offset = [112, 170]
Gohan_data = [Gohan_size, Gohan_scale, Gohan_offset]

#music and sounds
pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("assets/audio/punch.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
magic_fx.set_volume(0.75)

#load background image
bg_image = pygame.image.load("assets/images/background/bg2.jpg").convert_alpha()

#load spritesheets
Gon_sheet = pygame.image.load("assets/images/character 1/sprites/mhm.png").convert_alpha()
Gohan_sheet = pygame.image.load("assets/images/character2/sprites/wizard.png").convert_alpha()

#load vicory image
victory_img = pygame.image.load("assets/images/icons/BRRR.png").convert_alpha()

#define number of steps in each animation
GON_ANIMATION_STEPS = [3, 2, 4, 4, 5, 2, 4]
GOHAN_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

#define font
count_font = pygame.font.Font("assets/fonts/#44v2.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

class Game:

  #function for drawing text
  def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

  #function for drawing background
  def draw_bg():
    sized = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(sized, (0, 0))

  #function for drawing fighter health bars
  def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, SILVER, (x - 5, y - 5, 410, 60))
    pygame.draw.rect(screen, RED, (x, y, 400, 50))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 50))


  #create two instances of fighters
  fighter_1 = fighter(1, 200, 310, False, Gon_data, Gon_sheet, GON_ANIMATION_STEPS, sword_fx)
  fighter_2 = fighter(2, 700, 310, True, Gohan_data, Gohan_sheet, GOHAN_ANIMATION_STEPS, magic_fx)

  #game loop
  run = True
  while run:

    clock.tick(FPS)

    #draw background
    draw_bg()

    #show player stats
    draw_health_bar(fighter_1.health, 10, 20)
    draw_health_bar(fighter_2.health, 590, 20)
    draw_text("P1: " + str(score[0]), score_font, WHITE, 10, 70)
    draw_text("P2: " + str(score[1]), score_font, WHITE, 590, 70)

    #update countdown
    if intro_count <= 0:
      #move fighters
      fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
      fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
    else:
      #display count timer
      draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
      #update count timer
      if (pygame.time.get_ticks() - last_count_update) >= 1000:
        intro_count -= 1
        last_count_update = pygame.time.get_ticks()

    #update fighters
    fighter_1.update()
    fighter_2.update()

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #check for player defeat
    if round_over == False:
      if fighter_1.alive == False:
        score[1] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
      elif fighter_2.alive == False:
        score[0] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
    else:
      #display victory image
      screen.blit(victory_img, (170, 200))
      if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
        round_over = False
        intro_count = 3
        fighter_1 = fighter(1, 200, 310, False, Gon_data, Gon_sheet, GON_ANIMATION_STEPS, sword_fx)
        fighter_2 = fighter(2, 700, 310, True, Gohan_data, Gohan_sheet, GOHAN_ANIMATION_STEPS, magic_fx)

    #event handler
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        
  key = pygame.key.get_pressed()

  if key[pygame.K_p]:
    run == False
    if run == False:
      exec(open('pause.py').read())




    #update display
    pygame.display.update()

  #exit pygame
  pygame.quit()

