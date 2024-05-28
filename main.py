import pygame
from sys import exit
from random import randint, choice


pygame.init()
#measurements in pixels
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bernouli sim')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
start_time = 0


pipe = pygame.sprite.GroupSingle()
pipe.add(Pipe())
molecule_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
    screen.fill('lightblue')
    pipe.draw(screen)
    pipe.update()



    pygame.display.update()  
    clock.tick(60)