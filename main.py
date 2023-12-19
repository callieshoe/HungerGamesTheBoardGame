import pygame
import time
from pygame import mixer
import random
from player import playerOne, PlayerTwo, PlayerThree

pygame.init()
mixer.init()

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
pygame.display.set_caption('Hunger Games Board Game')




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
katniss_image = pygame.image.load('katniss.png')
rue_image = pygame.image.load('rue.png')
#transforming images to make them the same size
peta_image = pygame.transform.scale(peta_image, DefaultSize)
katniss_image = pygame.transform.scale(katniss_image, DefaultSize)
rue_image = pygame.transform.scale(rue_image, DefaultSize)
#text for above the images


#timer set up for pictures
display_time = 5
display2time = 10
display3time = 15
start_time = time.time()

#displaying the image loops
current_time = time.time()
if current_time - start_time < display_time:
    display_surface.fill((0,0,0))
    display_surface.blit(peta_image, (250,250))
    pygame.display.update()
elif current_time - start_time < display_time:
    display_surface.fill((0,0,0))
    display_surface.blit(katniss_image, (250,250))
    pygame.display.update()
elif current_time - start_time < display2time:
    display_surface.fill((0,0,0))
    display_surface.blit(rue_image, (250,250))
    pygame.display.update()
else:
    mixer.music.stop()



