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
       self.ypos = randint(start_point_Y_coord + self.cubelength, start_point_Y_coord + distance_within - self.cubelength)
       self.image = pygame.Surface((self.cubelength, self.cubelength))
       self.image.fill(self.color)
       self.image = self.image.convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.centerx = startXpos
       self.rect.centery = self.ypos
    def update(self):
       self.rect.x += self.velocity
       self.destroy()    
    def destroy(self):
        if self.rect.x >= 530:
            self.kill()
        
     


pygame.init()
#measurements in pixels
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bernouli sim')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)
small_font = pygame.font.Font('Pixeltype.ttf', 25)
start_time = 0

#parameters
molecular_velocity = 4
distance_within = 50
area = (distance_within / 200) ** 2 * math.pi
initial_pressure = 0
flowrate = round(area * molecular_velocity, 2)
startXpos = 230
start_point_X_coord = 230
end_point_X_coord = 530
start_point_Y_coord = 130

#objects
pipe = pygame.sprite.Group()
pipe.add(Pipe((start_point_X_coord, start_point_Y_coord), (end_point_X_coord, start_point_Y_coord), "black"))
pipe.add(Pipe((start_point_X_coord, start_point_Y_coord + distance_within), (end_point_X_coord, start_point_Y_coord + distance_within), "black"))
molecule_group = pygame.sprite.Group()

molecule_timer = pygame.USEREVENT + 1
pygame.time.set_timer(molecule_timer, 200)

#text
sim_name = test_font.render('Bernoulli\'s Equation: ', False, 'blue')
sim_name_rect = sim_name.get_rect(center = (400, 80))
sim_info = small_font.render(f'flowrate: {flowrate} m^3 / sec // cross-sectional area: {round(area, 2)} m^2 // water velocity: {molecular_velocity} m/s', False, 'blue')
sim_info_rect = sim_name.get_rect(center = (250, 120))

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
           molecule_group.add(Molecule(molecular_velocity))
    screen.fill('lightblue')
    screen.blit(sim_name, sim_name_rect)
    screen.blit(sim_info, sim_info_rect)
    pipe.draw(screen)
    pipe.update()
    molecule_group.draw(screen)
    molecule_group.update()



    pygame.display.update()  
    clock.tick(60)