import sys
import pygame
from random import randint

def display_score():
    current_time = pygame.time.get_ticks()//1000 - start_time//1000
    score_surf = test_font.render(str(current_time), False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list: #if our list is empty python will say that the list is False. But if it is True our list is not empty        
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5 

            if obstacle_rect.top == 150:
                screen.blit(fly_surface, obstacle_rect)
            else:
                screen.blit(snail_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collition(player_rect, obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            if player_rect.colliderect(obstacle):
                return False
    return True

pygame.init()#inizialice pygame, all the elements of pygame

#dispay surface, is the screen we are going to see
#width and height of the screen in tuple form
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")#Changing the window name

start_time = 0
score = 0
player_gravity = 0
clock = pygame.time.Clock()#creating an objet clock
game_active = False 
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)#(font type, font size)  

#sky
sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

#obstacles
    #snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
    #fly
fly_surface = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
obstacle_rect_list = []


#player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom= (100, 300))#takes a surface and draw a rectangle around it

#Start screen logo
playerStand_surface = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
playerStand_scaled = pygame.transform.scale2x(playerStand_surface)
playerStand_rect = playerStand_scaled.get_rect(center = (400, 200)) 

#Title game text
runner_game = test_font.render('Runner game', False, (111, 196, 169))
runner_game_rect = runner_game.get_rect(midbottom = (400, 50))

#Start message
start_message = test_font.render('Press SPACE to start', False, (111, 196, 169))
start_message_rect = start_message.get_rect(midbottom = (400, 320))

#timer
#This custom events are used to set timers.
#the set_timer method trigger our custom event in a certain times intervals.
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

#this is the game loop, we we will show our elements and update everything.
while True:
    #for loop, we will be looking for all player inputs until the input is to close the window
    for event in pygame.event.get(): #event.get will get us all the events in our game.
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:#check if some key is pressed
               if event.key == pygame.K_SPACE and player_rect.bottom == 300:#check if the key pressed is equal to the space
                    player_gravity = -22 

        else: 
            if event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_active:
            if randint(0,2):#two is not included 
                obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(midtop = (randint(900, 1100), 150)))
    if game_active:
        #attaching _surface to the display surface
        #putting surface on the Display surface
        #we choose the surface and the coordinates(x,y) in where the surface will be displayed
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        score = display_score()

        #snail
        #snail_rect.left -= 4
        #if snail_rect.left < -70: snail_rect.left = 800#if the position of the snail is equal to -70 start again from 840 
        #screen.blit(snail_surface, snail_rect)

        #player
        player_gravity += 1
        player_rect.top += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collition
        game_active = collition(player_rect, obstacle_rect_list)    
    else:
        screen.fill((94, 129, 162))
        screen.blit(playerStand_scaled, playerStand_rect)
        screen.blit(runner_game, runner_game_rect)
        obstacle_rect_list.clear()

        #score message
        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 380))

        if score == 0:
            screen.blit(start_message, start_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    #updates the display surface, we are putting all our elements in the screen we made
    pygame.display.update()
    clock.tick(60)#we said to the program that the while loop cant run faster than 60 times per second