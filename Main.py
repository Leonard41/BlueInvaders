# Importing Pygame
import pygame
import random
import math

# Initializate pygame
pygame.init()

# window size
screen_width = 800
screen_height = 600

# size variable

size = (screen_width, screen_height)

# Title
pygame.display.set_caption("Space Invaders by Leonardo Gonzalez")

# icon
icon = pygame.image.load("Sprites\Sprites\ship_4.png")
pygame.display.set_icon(icon)
# display_screen
screen = pygame.display.set_mode(size)

# bg image
background = pygame.image.load("9-2-space-picture.png")
# player function
player_x = 365
player_y = 520
player_img = pygame.image.load("Sprites\Sprites\ship_4.png")
player_x_change = 0
def player (x,y):
    screen.blit(player_img, (x,y))

# enemy function
enemy_x = random.randint(0,800)
enemy_y = random.randint(50,150)
enemy_img = pygame.image.load("Sprites\Sprites\ship_3.png")
enemy_x_change = 4
enemy_y_change = 40
def enemy (x,y):
    screen.blit(enemy_img, (x,y))

#bullet function
bullet_img = pygame.image.load("Sprites\Sprites\Bala del jugador.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = True

def fire(x,y):
    global bullet_state
    bullet_state = False
    screen.blit(bullet_img,(x,y))
# Collision
def is_collision (b_x, b_y, e_x, e_y):
    distance = math.sqrt((e_x - b_x)**2 + (e_y - b_y)**2)
    if distance < 27:
        return True
    else:
        return False




# game loop
running = True
clock = pygame.time.Clock()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE and bullet_state == True:
                bullet_x = player_x
                fire(player_x, bullet_y)
                bullet_state = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_change = -0
            if event.key == pygame.K_RIGHT:
                player_x_change = 0
                    
    screen.blit(background, (0, 0))

    player(player_x,player_y)

    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    # bullet blit

    if bullet_state == False:
        fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = True
    collision = is_collision(bullet_x, bullet_y, enemy_x, enemy_y)
    if collision:
        bullet_y = 480
        bullet_state = True
        enemy_x = random.randint(0, 735)
        enemy_y = random.randint(50, 150)

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = True
    # Enemy blit
    enemy(enemy_x,enemy_y)

        #enemy movements
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 4
        enemy_y += enemy_y_change

    elif enemy_x >= 736 :
        enemy_x_change = -4
        enemy_y += enemy_y_change

    clock.tick(60)
    pygame.display.update()
pygame.quit()







