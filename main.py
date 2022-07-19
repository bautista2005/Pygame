import sys
import pygame

def display_score():
    current_time = pygame.time.get_ticks()
    print(current_time)

pygame.init()#inizialice pygame, all the elements of pygame

#dispay surface, is the screen we are going to see
#width and height of the screen in tuple form
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")#Changing the window name

clock = pygame.time.Clock()#creating an objet clock

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)#(font type, font size)  
#score_surf = test_font.render('My game', False, 'black')
#score_rect = score_surf.get_rect(center= (400, 50))

game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom= (800, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom= (100, 300))#takes a surface and draw a rectangle around it

player_gravity = 0

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
                    snail_rect.left = 800

    if game_active:
        #attaching _surface to the display surface
        #putting surface on the Display surface
        #we choose the surface and the coordinates(x,y) in where the surface will be displayed
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        #pygame.draw.rect(screen, 'pink', score_rect)
        #pygame.draw.rect(screen, 'pink', score_rect, 10)
        #screen.blit(score_surf, score_rect)
        display_score()
        
        #snail
        snail_rect.left -= 4
        if snail_rect.left < -70: snail_rect.left = 800#if the position of the snail is equal to -70 start again from 840 
        screen.blit(snail_surface, snail_rect)

        #player
        player_gravity += 1
        player_rect.top += player_gravity

        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #collition
        if snail_rect.colliderect(player_rect):
            game_active = False        
    else:
        screen.fill('yellow')
    #updates the display surface, we are putting all our elements in the screen we made
    pygame.display.update()
    clock.tick(60)#we said to the program that the while loop cant run faster than 60 times per second
             