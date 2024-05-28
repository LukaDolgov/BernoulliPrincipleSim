import pygame
from sys import exit
from random import randint, choice


pygame.init()
#measurements in pixels
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bernouli sim')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)
start_time = 0


pipe = pygame.sprite.GroupSingle()
#pipe.add(Pipe())
molecule_group = pygame.sprite.Group()

molecule_timer = pygame.USEREVENT + 1
pygame.time.set_timer(molecule_timer, 1500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
      #  if event.type == molecule_timer:
           # molecule_group.add(Molecule())
    screen.fill('lightblue')
    pipe.draw(screen)
    pipe.update()
    molecule_group.draw(screen)
    molecule_group.update()



    pygame.display.update()  
    clock.tick(60)