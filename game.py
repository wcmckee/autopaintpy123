import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption('artcontrol.me: The Artwork Of William Mckee')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (121, 18, 38)
YELLOW = (210, 168, 54)
BLUE = (106, 14, 183)
GREEN = (44, 182, 53)


# set up fonts
HeadFont = pygame.font.SysFont(None, 48)
typeFont = pygame.font.SysFont(None, 12)

# set up the text
text = HeadFont.render('Hello world!', True, YELLOW, BLUE)
textRect = text.get_rect()
textRect.x = windowSurface.get_rect().centerx
textRect.y = windowSurface.get_rect().centery
# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw a green polygon onto the surface
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# draw some blue lines onto the surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# draw a red ellipse onto the surface
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# draw the text's background rectangle onto the surface
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# draw the text onto the surface
windowSurface.blit(text, textRect)

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
