import sys
import pygame

pygame.init()#inizialice pygame, all the elements of pygame

#dispay surface, is the screen we are going to see
#width and height of the screen in tuple form
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")#Changing the window name
<<<<<<< HEAD

clock = pygame.time.Clock()#creating an objet clock

test_surface = pygame.Surface((100, 200))
test_surface.fill("red")#"coloring" the test_surface
=======
clock = pygame.time.Clock()#creating an objet clockx
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)#(font type, font size)  
snail_x_pos = 840
snail_y_pos = 265

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surfaces = test_font.render('My game', False, 'black')
snail_surface = pygame.image.load('graphics/snail/snail1.png')
>>>>>>> d13f600 (second commit)

#this is the game loop, we we will show our elements and update everything.
while True:
    #for loop, we will be looking for all player inputs until the input is to close the window
    for event in pygame.event.get(): #event.get will get us all the events.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
<<<<<<< HEAD
    #attaching the test_surface to the display surface
    #putting test_surface on the Display surface
    #we choose the test_surface and the coordinates(x,y) in where the test surface will be displayed
    screen.blit(test_surface, (0,0))

=======
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surfaces, (325,50))

    snail_x_pos -= 4
    if snail_x_pos < -70: snail_x_pos = 840#if the position of the snail is equal to -70 start again from 840 
    screen.blit(snail_surface, (snail_x_pos, snail_y_pos))
>>>>>>> d13f600 (second commit)
    #updates the display surface, we are putting all our elements in the screen we made
    pygame.display.update()
    clock.tick(60)#we said to the program that the while loop cant run faster than 60 times per second