import pygame
from sys import exit
from random import randint, choice
import math

class Pipe(pygame.sprite.Sprite):
    def __init__(self, start_pos, end_pos, color, width=5):
        super().__init__()
        super().__init__()
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = width
        self.color = color

        # Calculate the length and angle of the line
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        length = math.hypot(dx, dy)
        angle = math.atan2(dy, dx)

        # Create a surface to draw the sloped rectangle
        self.image = pygame.Surface((length, width))
        self.image = self.image.convert_alpha()

        # Draw the sloped rectangle on the surface
        self.rect_points = [
            (0, -width // 2),
            (length, -width // 2),
            (length, width // 2),
            (0, width // 2)
        ]

        # Rotate the surface to match the angle of the line
        self.image = pygame.transform.rotate(self.image, -math.degrees(angle))
        self.rect = self.image.get_rect()

        # Set the position of the rect to be centered on the start_pos
        self.rect.midleft = start_pos

class Molecule(pygame.sprite.Sprite):
    def __init__(self, velocity):
       super().__init__()
       self.velocity = velocity
       self.xpos = startXpos
       self.color = "Blue"
       self.cubelength = 10
       self.ypos = randint(130 + 20, 130 + distance_within - self.cubelength)
       self.image = pygame.Surface((10, 10))
       self.image = self.image.convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.centerx = startXpos
       self.rect.centery = self.ypos
     


pygame.init()
#measurements in pixels
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bernouli sim')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)
start_time = 0

#parameters
molecular_velocity = 0
distance_within = 50
initial_pressure = 0
startXpos = 230

#objects
pipe = pygame.sprite.Group()
pipe.add(Pipe((230, 130), (530, 130), "black"))
pipe.add(Pipe((230, 130 + distance_within), (530, 130 + distance_within), "black"))
molecule_group = pygame.sprite.Group()

molecule_timer = pygame.USEREVENT + 1
pygame.time.set_timer(molecule_timer, 1500)

#text
sim_name = test_font.render('Bernoulli\'s Equation: ', False, 'blue')
sim_name_rect = sim_name.get_rect(center = (400, 80))

def return_pos():
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            return_pos()
        if event.type == molecule_timer:
           molecule_group.add(Molecule(1))
    screen.fill('lightblue')
    screen.blit(sim_name, sim_name_rect)
    pipe.draw(screen)
    pipe.update()
    molecule_group.draw(screen)
    molecule_group.update()



    pygame.display.update()  
    clock.tick(60)