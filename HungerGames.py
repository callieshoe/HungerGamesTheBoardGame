import pygame
import time
from pygame import mixer
import random 
from class_player import Player

pygame.init()
mixer.init()

# ... (other code)

start_time = time.time()

# RGB values of the colors 
black = (0, 0, 0)
green = (139, 0, 0)

# Assigning values to X and Y variables
X = 1200
Y = 800

#making screen
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Hungergames')

mixer.music.load('Cannon Sound (1).mp3')
mixer.music.play()
while mixer.music.get_busy():
    pygame.time.Clock().tick(10)
mixer.music.load('Theme song.mp3')
mixer.music.play()
  
pygame.time.Clock().tick(10)


font = pygame.font.Font('freesansbold.ttf', 25)

text = font.render('Welcome to the Hunger Games', True, green, black)
#text = font.render('The Hunger Games', True, green, black)

text2 = font.render('The rules', True, green, black)

textRect = text.get_rect()

# set to center of screen
textRect.center = (X // 2, Y // 2)

#setting up timer for the words so they p

display_time = 5
display2time = 10
start_time = time.time()
first = True


second = False


while first == True:
    # ... (other code)
    current_time = time.time()
    if current_time - start_time < display_time:
        display_surface.fill(black)
        display_surface.blit(text, textRect)
        pygame.display.update()
    elif current_time - start_time < display2time:
      display_surface.fill(black)
      display_surface.blit(text2, textRect)
      pygame.display.update()
    else:
      first = False
      second = True






#second part
text = font.render('Roll the dice.Move forward how everymany you rolled. Clame your fate.', True, green, black)
#text = font.render('The Hunger Games', True, green, black)

text2 = font.render('May the odds be ever in your favor!', True, green, black)

display_time = 5
display2time = 10
start_time = time.time()
second = True
while second == True:
    # ... (other code)
    current_time = time.time()
    if current_time - start_time < display_time:
        font = pygame.font.Font('freesansbold.ttf', 2)
        display_surface.fill(black)
        display_surface.blit(text, (300,(Y//2)))
        pygame.display.update()
    elif current_time - start_time < display2time:
      font = pygame.font.Font('freesansbold.ttf', 25)
      display_surface.fill(black)
      display_surface.blit(text2, textRect)
      pygame.display.update()
    else:
      first = False
      break


#end of intro start introducing charecters and their districts

text = font.render('INTRODUCING THE TRIBUTES', True, green, black)




display_time = 5
display2time = 10
start_time = time.time()

start_time = time.time()
third = True
while third == True:
   
    current_time = time.time()
    if current_time - start_time < display_time:
        font = pygame.font.Font('freesansbold.ttf', 10)
        display_surface.fill(black)
        display_surface.blit(text, textRect)
        pygame.display.update()
    else:
       break
    



#end of intro start introducing charecters and their districts
#importing the images and making them the same size
DefaultSize = (500,500)

peta_image = pygame.image.load('peta.png')
clove_image = pygame.image.load('clove.png')
cato_image = pygame.image.load('cato.png')
katniss_image = pygame.image.load('katniss.png')
gale_image = pygame.image.load('gale.png')
finnick_image = pygame.image.load('finnick.png')
rue_image = pygame.image.load('rue.png')
#transforming images to make them the same size
peta_image = pygame.transform.scale(peta_image, DefaultSize)
clove_image = pygame.transform.scale(clove_image, DefaultSize)
cato_image = pygame.transform.scale(cato_image, DefaultSize)  
katniss_image = pygame.transform.scale(katniss_image, DefaultSize)
gale_image = pygame.transform.scale(gale_image, DefaultSize)
finnick_image = pygame.transform.scale(finnick_image, DefaultSize)
rue_image = pygame.transform.scale(rue_image, DefaultSize)
#text for above the images


#timer set up for pictures
display_time = 5
display2time = 10
display3time = 15
display4time = 20
display5time = 25
display6time = 30
display7time = 35
start_time = time.time()

#displaying the image loops 
while True:
  current_time = time.time()
  if current_time - start_time < display_time:
   display_surface.fill((0,0,0))
   display_surface.blit(peta_image, (250,250))
   pygame.display.update()
  elif current_time - start_time < display2time:
   
    display_surface.fill((0,0,0))
    display_surface.blit(clove_image, (250,250))
    pygame.display.update()
  elif current_time - start_time < display3time:
    
    display_surface.fill((0,0,0))
    display_surface.blit(cato_image, ((250,250)))
    pygame.display.update()
  elif current_time - start_time < display4time:
    
    display_surface.fill((0,0,0))
    display_surface.blit(katniss_image, (250,250))
    pygame.display.update()
  elif current_time - start_time < display5time:
    
    display_surface.fill((0,0,0))
    display_surface.blit(rue_image, (250,250))
    pygame.display.update()
  elif current_time - start_time < display6time:
    
    display_surface.fill((0,0,0))
    display_surface.blit(gale_image, (250,250))
    pygame.display.update()
  elif current_time - start_time < display7time:
    
    display_surface.fill((0,0,0))
    display_surface.blit(finnick_image, (250,250))
    pygame.display.update()
  else:
     break
     
    
mixer.music.stop()
  
  


#charecters
charecters = ["Katniss","Peeta","Rue","Finnick","Gale","Cato","Clove"]
random.shuffle(charecters)

#square values and their consequencces
square_consequences = {
    2: 50,
    4: 50,
    20: 50,
    17: 50,
    5: 15,
    8: 15,
    9: 15,
    11: 15,
    12: 15,
    15: 15,
    16: 15,
    21: 15,
    22: 15,
    18: -50,
    3: -100,
    6: -100,
    10: -100,
    14: -100,
    23: -100,
    24: -100
}

while True:
  font = pygame.font.Font(None, 36)
  #loading board
  board = pygame.image.load('board.png')
  board = pygame.transform.scale(board, (X, Y))
  display_surface.blit(board, (50, 50))
  pygame.display.update()
  #start of with 3 players 
  #player,health,curent square
  players = [Player(charecters[i], 100,1) for i in range(3)]  
  #randomly selected characters
  for i, player in enumerate(players): 
    # Display each player's character on the screen
    text = font.render(f"Player {i+1}: {player.name}", True, (255, 255, 255))
    display_surface.blit(text, (800, 100 + 100 * i))
  pygame.display.update()





  #making dice function
  def roll_dice(display_surface, font):
    roll = random.randint(1, 6)
    #adding the number rolled to current square
    for player in players:
      
      player.current_square += roll
      #resetting square value when gets to end of the board
      if player.current_square <= 24:
        player.current_square = (player.current_square % 24)
        if player.current_square == 0:
          player.current_square =  1
      #health system
      if player.current_square in square_consequences:
        player.health += square_consequences[player.current_square]
        health_text = font.render(f"Player {i+1}'s health: {player.health}" , True, (255, 255, 255))
        display_surface.blit(health_text, (800, 700))
        #checking if player dead
        if player.health <= 0:
          player.alive = False
      #displang what player rolled
      text = font.render(f"Player rolled: {roll}", True, (255, 255, 255))
      display_surface.blit(text, (800, 500))
      #displaying players square
      suqare_text = font.render(f"Player {i+1}'s current square: {player.current_square}" , True, (255, 255, 255))
      display_surface.blit(suqare_text, (800, 600))
      pygame.display.update()
      
    #health system
      

  #making button
  button_width = 110
  button_height = 50
  button_color = (139, 0, 0)
  button_text = "Roll Dice"
  pygame.draw.rect(display_surface, button_color, (800, 400, button_width, button_height))
  text = font.render(button_text, True, (255, 255, 255))
  display_surface.blit(text, (800, 415))
  pygame.display.update()


  #pushing button
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        if 800 <= mouse_pos[0] <= 910 and 400 <= mouse_pos[1] <= 450:
            roll_dice(display_surface, font)
            pygame.display.update()
            time.sleep(3)