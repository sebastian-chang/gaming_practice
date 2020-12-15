import pygame
import sys
import random
from pygame.locals import *

# Set up pygame
pygame.init()
main_clock = pygame.time.Clock()

# Set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up the player and food data structures
food_counter = 0
NEW_FOOD = 40
FOOD_SIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - FOOD_SIZE),
                             random.randint(0, WINDOW_HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE))

# Set up movement variables
move_left = False
move_right = False
move_up = False
move_down = False

MOVE_SPEED = 6


# Run the game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change teh keyboard variables
            if event.key == K_LEFT or event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_RIGHT or event.key == K_d:
                move_left = False
                move_right = True
            if event.key == K_UP or event.key == K_w:
                move_down = False
                move_up = True
            if event.key == K_DOWN or event.key == K_s:
                move_up = False
                move_down = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                move_left = False
            if event.key == K_RIGHT or event.key == K_d:
                move_right = False
            if event.key == K_UP or event.key == K_w:
                move_up = False
            if event.key == K_DOWN or event.key == K_s:
                move_down = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOW_HEIGHT - player.height)
                player.left = random.randint(0, WINDOW_WIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(
                event.pos[0], event.pos[1], FOOD_SIZE, FOOD_SIZE))

    food_counter += 1
    if food_counter >= NEW_FOOD:
        # Add new food
        food_counter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - FOOD_SIZE),
                                 random.randint(0, WINDOW_HEIGHT - FOOD_SIZE), FOOD_SIZE, FOOD_SIZE))

    # Draw the white background onto the sruface
    window_surface.fill(WHITE)

    # Move the player
    if move_down and player.bottom < WINDOW_HEIGHT:
        player.top += MOVE_SPEED
    if move_up and player.top > 0:
        player.top -= MOVE_SPEED
    if move_left and player.left > 0:
        player.left -= MOVE_SPEED
    if move_right and player.right < WINDOW_WIDTH:
        player.left += MOVE_SPEED

    # Draw the player onto the surface
    pygame.draw.rect(window_surface, BLACK, player)

    # Check whether the player has intersected with any food squares
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    # Draw the food
    for i in range(len(foods)):
        pygame.draw.rect(window_surface, GREEN, foods[i])

    # Draw the window onto the screen
    pygame.display.update()
    main_clock.tick(40)
