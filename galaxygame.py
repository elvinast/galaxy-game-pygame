import pygame
import random
import time
import math

pygame.init()
pygame.font.init()


dist = 0
done = False
score = 0
life = 3

#-------MAIN---------
fonts = pygame.font.get_fonts()

screen = pygame.display.set_mode((800, 600))
backgroundImage = pygame.image.load("bgbg.png")
pygame.display.set_caption("K I L L   T H E   A L I E N")
gameIcon = pygame.image.load('logo.png')
pygame.display.set_icon(gameIcon)
font = pygame.font.SysFont('Times new roman', 32) 
lifeIcon = pygame.image.load('heart.png')

#-------BULLET--------
bulcnt = 0
gameBullet = pygame.image.load('pulya.png')
bul_x = 220
bul_y = 460
bul_dx = 0
bul_dy = 0

#-------PLAYER--------
playerImage = pygame.image.load("pl.png")
player_x = 200
player_y = 500


#-------ENEMY---------
enemyImage = pygame.image.load("enem.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(20, 50)
enemy_dx = 5
enemy_dy = 60


#----To show score on the screen-------
def scores (x,y):
    res = font.render('s c o r e:  ' + str(score), True, (255, 255, 0)) #draw text on a new Surf
    screen.blit(res, (x,y))

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def bullet(x,y):
    screen.blit(gameBullet, (x, y))
    
#----to check the collision
def hits(enemy_x, enemy_y, bul_x, bul_y):
    if bul_x in range(enemy_x, enemy_x + 70) and bul_y in range(enemy_y, enemy_y + 70):
        return True
    return False

def lose(enemy_y):
    if enemy_y > 400:
        return True
    return False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed() 

    if pressed[pygame.K_LEFT]: 
        player_x -= 5
        bul_x -= 5

    if pressed[pygame.K_RIGHT]: 
        player_x += 5 #границы
        bul_x += 5

    
    if (player_x < 0 or player_x > 800) and (bul_x < 0 or bul_x > 800):
        if bul_y < 460:
            player_x = (player_x + 800) % 800 
        elif bul_y == 460:
            player_x = (player_x + 800) % 800
            bul_x = (bul_x + 800) % 800 

    
    enemy_x += enemy_dx
    if enemy_x < 0 or enemy_x > 736:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy

    screen.blit(backgroundImage, (0, 0))
    
    if bul_x == player_x + 20 and bul_y == 460:
        pos_player = player_x

    if pressed[pygame.K_SPACE]:
        bulcnt = 1
    if bulcnt == 1:
        bul_y -= 5
        bul_x = pos_player + 20

    if bul_y == 0:
        bulcnt = 0
        life -= 1
        bul_x = player_x + 20
        bul_y = 460

    #hitting
    hit = hits(enemy_x, enemy_y, bul_x, bul_y)
    if hit and bul_y < 460:
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(20, 50)
        bul_y = 460
        bul_x = player_x + 20
        score += 1
        bulcnt = 0

    if lose(enemy_y) or life == 0:
        if life > 1:
            life -= 1
            enemy_x = random.randint(0, 736)
            enemy_y = random.randint(20, 50)
        else:
            screen.fill((234, 137, 154))
            res = font.render('G A M E   O V E R!', True, (0, 0, 0))
            res1 = font.render('T O T A L   S C O R E : ' + str(score), True, (0,0,0))
            screen.blit(res, (250,250))
            screen.blit(res1, (250,300))
            # enemy_x = 730
            # enemy_y = 0
            enemy_dx = 0
            enemy_dy = 0
            enemy_x = 250
            enemy_y = 450
            player_x = 350
            player_y = 450
            bul_x = 370
            bul_y = 410
            
    
    if life == 3:
        screen.blit(lifeIcon, (620, 20))
        screen.blit(lifeIcon, (660, 20))
        screen.blit(lifeIcon, (700, 20))
    if life == 2:
        screen.blit(lifeIcon, (660, 20))
        screen.blit(lifeIcon, (700, 20))
    if life == 1:
        screen.blit(lifeIcon, (700, 20))


    res = font.render(str(life), True, (200, 200, 0))
    screen.blit(res, (750,20))

    enemy(enemy_x, enemy_y)
    player(player_x, player_y)
    bullet(bul_x, bul_y)
    scores(625,60)
    pygame.display.update()
