import pygame, sys
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up the window.
window_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello World!')

# Set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the fonts
basic_font = pygame.font.Font(None, 48)

# Set up the text
text = basic_font.render('Hello World!', True, WHITE, BLUE)
text_rect = text.get_rect()
text_rect.centerx = window_surface.get_rect().centerx
text_rect.centery = window_surface.get_rect().centery

# Draw the white background onto the surface
window_surface.fill(WHITE)

# Draw a green polygon onto the surface
# surface, color, (x, y) points for each corner of polygon
pygame.draw.polygon(window_surface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw some blue lines onto the surface
# surface, color, (starting point), (end point), line thickness
pygame.draw.line(window_surface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(window_surface, BLUE, (120, 60), (60, 120))
pygame.draw.line(window_surface, BLUE, (60, 120), (120, 120), 4)

# Draw a blue circle onto the surface
# surface, color, (center point), radius of circle, fill of circle
pygame.draw.circle(window_surface, BLUE, (300, 50), 20, 0)

# Draw a red ellipse onto the surface
# surface, color, (left, top, width, height) of ellipse, line thickness
pygame.draw.ellipse(window_surface, RED, (300, 250, 40, 80), 1)

# Draw the text's background rectangle onto the surface
# surface, color, (left, top *corner of rect*, width, height)
pygame.draw.rect(window_surface, RED, (text_rect.left - 20, text_rect.top - 20, text_rect.width + 40, text_rect.height + 40))

# Get a pixel array of the surface
pixal_array = pygame.PixelArray(window_surface)
pixal_array[480][360] = BLACK
del pixal_array

# Draw the text onto the surface
window_surface.blit(text, text_rect)

# Draw the window onto the screen
pygame.display.update()

# Run the game loop
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
