import pygame
import sys
import time
import random
import os
from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sounds')

# Set up the colors
WHITE = (255, 255, 255)

# Set up the block data structure
player = pygame.Rect(300, 100, 40, 40)
player_image = pygame.image.load(os.path.join(
    os.path.dirname(__file__), 'images', 'player.png')).convert()
player_stretched_image = pygame.transform.scale(player_image, (40, 40))
food_image = pygame.image.load(os.path.join(
    os.path.dirname(__file__), 'images', 'cherry.png')).convert()
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - 20),
                             random.randint(0, WINDOW_HEIGHT - 20), 20, 20))

food_counter = 0
NEW_FOOD = 40

# Set up keyboard variables
move_left = False
move_right = False
move_up = False
move_down = False

MOVE_SPEED = 6

# Set up the music
pick_up_sound = pygame.mixer.Sound(os.path.join(
    os.path.dirname(__file__), 'sounds', 'pickup.wav'))
pygame.mixer.music.load(os.path.join(
    os.path.dirname(__file__), 'sounds', 'background.mid'))
pygame.mixer.music.play(-1, 0.0)
music_is_playing = True

# Run the game loop
while True:
    # Check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables
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
            if event.key == K_m:
                if music_is_playing:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                music_is_playing = not music_is_playing

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(
                event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    food_counter += 1
    if food_counter >= NEW_FOOD:
        # Add new food
        food_counter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOW_WIDTH - 20),
                                 random.randint(0, WINDOW_HEIGHT - 20), 20, 20))

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

    # Draw the block onto the surface
    window_surface.blit(player_stretched_image, player)

    # Check whether the block has intersected with any food squares
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top,
                                 player.width + 2, player.height + 2)
            player_stretched_image = pygame.transform.scale(
                player_image, (player.width, player.height))
            if music_is_playing:
                pick_up_sound.play()

    # Draw the food
    for food in foods:
        window_surface.blit(food_image, food)

    # Draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
