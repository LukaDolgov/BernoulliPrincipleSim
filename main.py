import pygame
from sys import exit
from random import randint, choice
import math

class Pipe(pygame.sprite.Sprite):
    def __init__(self, start_pos, end_pos, color, width=5, ismovable=False):
        super().__init__()
        super().__init__()
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = width
        self.color = color
        self.ismovable = ismovable

        # Calculate the length and angle of the line
        self.dx = end_pos[0] - start_pos[0]
        self.dy = end_pos[1] - start_pos[1]
        length = math.hypot(self.dx, self.dy)
        angle = math.atan2(self.dy, self.dx)

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
        self.rect.center = (start_pos[0] + self.dx/2, start_pos[1] + self.dy/2)
    

class Molecule(pygame.sprite.Sprite):
    def __init__(self, velocity):
       super().__init__()
       self.velocity = velocity
       self.xpos = startXpos
       self.color = "Blue"
       self.cubelength = 10
       if sim_mode == 1:
         self.ypos = randint(start_point_Y_coord + self.cubelength, start_point_Y_coord + distance_within * 10 - self.cubelength)
       elif sim_mode == 2:
         self.ypos = randint(start_point_Y_coord_2 + self.cubelength, start_point_Y_coord_2 + distance_within * 10 - self.cubelength)  
       self.image = pygame.Surface((self.cubelength, self.cubelength))
       self.image.fill(self.color)
       self.image = self.image.convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.centerx = startXpos
       self.rect.centery = self.ypos
       self.count = 0
    def posUpdate(self):
        if sim_mode == 2:
            for pipe in pipe_new:
                    if pipe.ismovable == True and pipe.start_pos != (end_point_X_coord_2, start_point_Y_coord_2):
                        selectedpipe = pipe
            for pipe in pipe_new:
                    if pipe.ismovable == False and pipe.start_pos == (end_point_X_coord_2, start_point_Y_coord_2):
                        otherselectedpipe = pipe
            adjustable_y = -1 * (calculate_slope(otherselectedpipe)) * (self.count) * 4 + start_point_Y_coord_2
            if self.xpos >= end_point_X_coord_2 and self.xpos <= end_point_X_coord_3:
                self.count += 1
                if self.velocity >= 2:
                    self.rect.y -= (calculate_slope(selectedpipe)) * (self.count * self.velocity / 4)
                    self.ypos -= (calculate_slope(selectedpipe)) * (self.count * self.velocity / 4) 
                else:
                    self.rect.y -= (calculate_slope(selectedpipe)) * (self.count + 3 / self.count)
                    self.ypos -= (calculate_slope(selectedpipe)) * (self.count + 3 / self.count)
            elif self.xpos >= end_point_X_coord_3:
                self.rect.y -= 0
                self.ypos -= 0 
            if self.xpos >= end_point_X_coord_2 and self.xpos <= end_point_X_coord_3 and self.ypos <= adjustable_y:
                self.ypos = randint(int(adjustable_y) + self.cubelength, int(adjustable_y) + 50 - self.cubelength)  
                self.rect.y = self.ypos    
            if self.xpos >= end_point_X_coord_3 and self.xpos <= end_point_X_coord_4 and self.ypos >= end_point_Y_coord + 40:
                self.ypos = randint(end_point_Y_coord + self.cubelength, end_point_Y_coord + 50 - self.cubelength * 2)  
                self.rect.y = self.ypos
            if self.xpos >= end_point_X_coord_3 and self.xpos <= end_point_X_coord_4 and self.ypos <= end_point_Y_coord:
                self.ypos = randint(end_point_Y_coord + self.cubelength, end_point_Y_coord + 50 - self.cubelength * 2)  
                self.rect.y = self.ypos
    def update(self):
       self.rect.x += self.velocity
       self.xpos += self.velocity
       self.destroy()
       self.posUpdate()    
    def destroy(self):
        if self.rect.x >= 530 and sim_mode ==1:
            self.kill()
        elif self.rect.x >= 700:
            self.kill()
        
     

#sim info
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Bernouli sim')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)
small_font = pygame.font.Font('Pixeltype.ttf', 25)
start_time = 0
sim_mode = 1

#parameters
molecular_velocity = 4
distance_within = 5
area = (distance_within / 20) ** 2 * math.pi
initial_pressure = 0
flowrate = round(area * molecular_velocity, 2)
startXpos = 230
start_point_X_coord = 230
end_point_X_coord = 530
start_point_Y_coord = 130


start_point_Y_coord_2 = 200
end_point_Y_coord = 150

start_point_X_coord_2 = 230
end_point_X_coord_2 = 430
end_point_X_coord_3 = 530
end_point_X_coord_4 = 700

#objects
pipe = pygame.sprite.Group()
pipe.add(Pipe((start_point_X_coord, start_point_Y_coord), (end_point_X_coord, start_point_Y_coord), "black"))
pipe.add(Pipe((start_point_X_coord, start_point_Y_coord + distance_within * 10), (end_point_X_coord, start_point_Y_coord + distance_within * 10), "black"))
molecule_group = pygame.sprite.Group()

pipe_new = pygame.sprite.Group()
pipe_new.add(Pipe((start_point_X_coord_2, start_point_Y_coord_2), (end_point_X_coord_2, start_point_Y_coord_2), "black"))
pipe_new.add(Pipe((start_point_X_coord_2, start_point_Y_coord_2 + distance_within * 10), (end_point_X_coord_2, start_point_Y_coord_2 + distance_within * 10), "black", 5, True))
pipe_new.add(Pipe((end_point_X_coord_2, start_point_Y_coord_2), (end_point_X_coord_3, end_point_Y_coord), "black"))
pipe_new.add(Pipe((end_point_X_coord_2, start_point_Y_coord_2  + distance_within * 10), (end_point_X_coord_3, end_point_Y_coord + distance_within * 10), "black", 5, True))
pipe_new.add(Pipe((end_point_X_coord_3, end_point_Y_coord), (end_point_X_coord_4, end_point_Y_coord), "black"))
pipe_new.add(Pipe((end_point_X_coord_3, end_point_Y_coord + 50), (end_point_X_coord_4, end_point_Y_coord + 50), "black"))
molecule_group_new = pygame.sprite.Group()

molecule_timer = pygame.USEREVENT + 1
pygame.time.set_timer(molecule_timer, 50)

#text + arrows screen 1
sim_name = test_font.render('Flow Rate Relation: dV/dt = A * dX/dt', False, 'blue')
sim_name_rect = sim_name.get_rect(center = (400, 80))
sim_info_rect = sim_name.get_rect(center = (320, 120))
sim_info_rect_new = sim_name.get_rect(midleft = (50, 95))
sim_vars = test_font.render('Parameters: ', False, 'blue')
sim_vars_rect = sim_name.get_rect(center = (280, 200))
param_1 =  small_font.render('Area', False, 'blue')
param_1_rect = param_1.get_rect(center = (80, 275))
param_2 =  small_font.render('Velocity', False, 'blue')
param_2_rect = param_2.get_rect(center = (190, 275))
arrowdown = pygame.image.load('graphics/arrow1.png').convert_alpha()
arrowdown = pygame.transform.rotozoom(arrowdown, 0, .2)
arrowup = pygame.transform.rotozoom(arrowdown, 180, 1)
arrowsdown = []
arrowsup = []

#text + arrows screen 2
sim_name_new = test_font.render('Bernouli\'s Equation: ', False, 'blue')
sim_name_new_rect = sim_name.get_rect(midleft = (50, 40))
explain_equation = small_font.render('P + pgh + 1/2pv^2 = constant, P= pressure, p=density of fluid, v=velocity of fluid', False, 'blue')
explain_equation_rect = explain_equation.get_rect(midleft = (50, 70))
extra_info = small_font.render('*not optimized for velocity less than 2 m/s because of Pygame rounidng*', False, 'blue')
extra_info_rect = extra_info.get_rect(midleft = (50, 110))

#change screen button
change_screen_surface = pygame.Surface((200, 50))
change_screen_surface.fill("blue")
change_screen_surface_rect = change_screen_surface.get_rect(center = (670, 300))
inside_box = pygame.Surface((180, 40))
inside_box_rect = inside_box.get_rect(center = (100, 25))
inside_box.fill("black")
text_surface = small_font.render("change sim", True, 'blue')
text_rect = text_surface.get_rect(center=(100, 25))
change_screen_surface.blit(inside_box, inside_box_rect)
change_screen_surface.blit(text_surface, text_rect)


def getarrowdown_rect(i):
    arrowsdown.append(arrowdown.get_rect(midtop = (41 + 100 * i, 274)))
    return arrowdown.get_rect(midtop = (41 + 100 * i, 274))
def getarrowup_rect(i):
    arrowsup.append(arrowup.get_rect(midbottom = (41 + 100 * i, 270)))
    return arrowup.get_rect(midbottom = (41 + 100 * i, 270))
def return_pos():
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
def calculate_slope(pipe):
    dx = pipe.dx
    dy = pipe.dy
    return (dy / dx) * -1
def click_arrow():
    mouse_pos = pygame.mouse.get_pos()
    global distance_within, molecular_velocity, area, sim_mode
    if sim_mode == 1:
        if arrowsdown[0].collidepoint(mouse_pos) and pygame.mouse.get_pressed() and distance_within > 5:
            distance_within -= 5
            area -= .1
            sprite_to_remove = pipe.sprites()[1]
            pipe.remove(sprite_to_remove)
            pipe.add(Pipe((start_point_X_coord, start_point_Y_coord + distance_within * 10), (end_point_X_coord, start_point_Y_coord + distance_within * 10), "black"))
        if arrowsup[0].collidepoint(mouse_pos) and pygame.mouse.get_pressed():
            distance_within += 5
            area += .1
            sprite_to_remove = pipe.sprites()[1]
            pipe.remove(sprite_to_remove)
            pipe.add(Pipe((start_point_X_coord, start_point_Y_coord + distance_within * 10), (end_point_X_coord, start_point_Y_coord + distance_within * 10), "black"))
        if arrowsdown[1].collidepoint(mouse_pos) and pygame.mouse.get_pressed():
            molecular_velocity -= .5
            print(molecular_velocity)
        if arrowsup[1].collidepoint(mouse_pos) and pygame.mouse.get_pressed():
            molecular_velocity += .5
            print(molecular_velocity)
    if change_screen_surface_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed():
        if sim_mode >= 2: 
          sim_mode = 1
          molecule_group.empty()
          molecule_group_new.empty()
        else: 
          sim_mode += 1
          molecule_group.empty()
          molecule_group_new.empty()
    if sim_mode == 2:
        if arrowsdown[0].collidepoint(mouse_pos) and pygame.mouse.get_pressed() and distance_within > 5:
            distance_within -= 5
            area -= .1
            for sprite in pipe_new:
                if sprite.ismovable == True:
                    pipe_new.remove(sprite)
            pipe_new.add(Pipe((start_point_X_coord_2, start_point_Y_coord_2 + distance_within * 10), (end_point_X_coord_2, start_point_Y_coord_2 + distance_within * 10), "black", 5, True))
            pipe_new.add(Pipe((end_point_X_coord_2, start_point_Y_coord_2  + distance_within * 10), (end_point_X_coord_3, end_point_Y_coord + 50), "black", 5, True))

        if arrowsup[0].collidepoint(mouse_pos) and pygame.mouse.get_pressed():
            distance_within += 5
            area += .1
            for sprite in pipe_new:
                if sprite.ismovable == True:
                    pipe_new.remove(sprite)
            pipe_new.add(Pipe((start_point_X_coord_2, start_point_Y_coord_2 + distance_within * 10), (end_point_X_coord_2, start_point_Y_coord_2 + distance_within * 10), "black", 5, True))
            pipe_new.add(Pipe((end_point_X_coord_2, start_point_Y_coord_2  + distance_within * 10), (end_point_X_coord_3, end_point_Y_coord + 50), "black", 5, True))

        if arrowsdown[1].collidepoint(mouse_pos) and pygame.mouse.get_pressed():
            molecular_velocity -= .5
            print(molecular_velocity)
        if arrowsup[1].collidepoint(mouse_pos) and pygame.mouse.get_pressed():
            molecular_velocity += .5
            print(molecular_velocity) 
        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            return_pos()
            click_arrow()
        if event.type == molecule_timer:
           for i in range(int(molecular_velocity)):
               molecule_group.add(Molecule(molecular_velocity))
               molecule_group_new.add(Molecule(molecular_velocity))
    if sim_mode == 1:
        screen.fill('lightblue')
        screen.blit(sim_name, sim_name_rect) 
        screen.blit(sim_vars, sim_vars_rect)
        pipe.draw(screen)
        pipe.update()
        molecule_group.draw(screen)
        molecule_group.update()
        for i in range(2):
            screen.blit(arrowdown, getarrowdown_rect(i))
            screen.blit(arrowup, getarrowup_rect(i))
        screen.blit(param_1, param_1_rect)
        screen.blit(param_2, param_2_rect)
        flowrate = round(area * molecular_velocity, 2)
        sim_info = small_font.render(f'flowrate: {flowrate} m^3 / sec // cross-sectional area: {round(area, 2)} m^2 // water velocity: {molecular_velocity} m/s', False, 'blue')
        screen.blit(sim_info, sim_info_rect)
        screen.blit(change_screen_surface, change_screen_surface_rect)
    elif sim_mode == 2: 
        screen.fill("lightblue")
        screen.blit(sim_name_new, sim_name_new_rect) 
        screen.blit(explain_equation, explain_equation_rect)
        screen.blit(change_screen_surface, change_screen_surface_rect)
        for i in range(2):
            screen.blit(arrowdown, getarrowdown_rect(i))
            screen.blit(arrowup, getarrowup_rect(i))
            screen.blit(param_1, param_1_rect)
            screen.blit(param_2, param_2_rect)
        flowrate = round(area * molecular_velocity, 2)
        sim_info = small_font.render(f'flowrate: {flowrate} m^3 / sec // cross-sectional area: {round(area, 2)} m^2 // water velocity: {molecular_velocity} m/s', False, 'blue')
        screen.blit(sim_info, sim_info_rect_new)
        screen.blit(extra_info, extra_info_rect)
        pipe_new.draw(screen)
        pipe_new.update()
        molecule_group_new.draw(screen)
        molecule_group_new.update()
        
    pygame.display.update()  
    clock.tick(60)