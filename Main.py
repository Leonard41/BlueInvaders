# Importing Pygame
import pygame
import random
import math

from pygame import mixer

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

# background sound
mixer.music.load("y2mate.com-Hotline-Miami-2-Wrong-Number-Soundtrack-Bloodline.wav")
mixer.music.play (-1)


# display_screen
screen = pygame.display.set_mode(size)

# Score font
score_font = pygame.font.Font("Minecraft.ttf", 32)

# variable score
score= 0

# position text in screen
text_x = 10
text_y = 10

# game over font
go_x = 305
go_y = 265
# condicion de una vez game over
go_condicion = True

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
enemy_x = []
enemy_y = []
enemy_img = []
enemy_x_change = []
enemy_y_change = []
number_enemies = 30
for item in range(number_enemies):
    enemy_img.append(pygame.image.load("Sprites\Sprites\ship_3.png"))
    enemy_x.append(random.randint(0,735))
    enemy_y.append(random.randint(50,150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)
def enemy (x,y, item):
    screen.blit(enemy_img[item], (x,y))

#bullet function
bullet_img = pygame.image.load("11.png")
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
        
    
def game_over(x,y):
    global go_condicion
    go_text = score_font.render("GAME OVER",True, (0,71,255))
    
        # game over sound
    if go_condicion :
        game_over_sound = mixer.Sound("kl-peach-game-over-i-132096_1.wav")
        game_over_sound.play()
        go_condicion = False
    screen.blit (go_text, (x,y))

def show_score(x,y):
        score_text = score_font.render("SCORE:  " + str(score),True, (255,255,255))
        screen.blit (score_text, (x,y))
    





# game loop
running = True
clock = pygame.time.Clock()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -10
            if event.key == pygame.K_RIGHT:
                player_x_change = 10
            if event.key == pygame.K_SPACE and bullet_state == True:
                bullet_x = player_x
                #bullet sound
                bullet_sound = mixer.Sound("retro_laser_gun_shot-96367_1.wav")
                bullet_sound.play()
                fire(player_x, bullet_y)

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
    
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = True
    for item in range ( number_enemies ):

        if enemy_y[item] >= 440:
            for j in range (number_enemies):
                enemy_y[j] = 2000
            game_over(go_x,go_y)
            break
        collision = is_collision(bullet_x, bullet_y, enemy_x[item], enemy_y[item])
        if collision:
            bullet_y = 480
            bullet_state = True
            score += 200
            enemy_x[item] = random.randint(0, 735)
            enemy_y[item] = random.randint(50, 150)
            collision_sound = mixer.Sound("small-explosion-129477.wav")
            collision_sound.play()
            

        # Enemy blit
        enemy(enemy_x[item],enemy_y[item], item)

            #enemy movements
        enemy_x[item] += enemy_x_change[item]
        if enemy_x[item] <= 0:
            enemy_x_change[item] = 4
            enemy_y[item] += enemy_y_change[item]

        elif enemy_x[item] >= 736 :
            enemy_x_change[item] = -4
            enemy_y[item] += enemy_y_change[item]

    show_score(text_x, text_y)
    clock.tick(60)
    pygame.display.update()
pygame.quit()







