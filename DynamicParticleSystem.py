import pygame
import random
import math

pygame.init()
pygame.display.set_caption('Particle System')

# Initialize variables
run = True
fps = 60
Clock = pygame.time.Clock()
background_color = (20, 20, 20)
screen_size = (1000, 1000)
screen = pygame.display.set_mode(screen_size)
polygon_array = []

# Define Polygon class
class Polygon:
    def __init__(self, position, velocity, radius, poly_count, color, life_time):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.poly_count = poly_count
        self.color = color
        self.life_time = 1/life_time

    def update_polygon(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.velocity[1] += 0.1
        self.radius -= self.life_time
        if self.radius <= 0:
            polygon_array.remove(self)

    def draw_polygon(self):
        polygon_angle = 2 * math.pi / self.poly_count
        polygon_points = []
        for i in range(self.poly_count):
            x = int(self.position[0] + self.radius * math.cos(polygon_angle * i))
            y = int(self.position[1] + self.radius * math.sin(polygon_angle * i))
            polygon_points.append((x, y))
        pygame.draw.polygon(screen, self.color, polygon_points)

# Called Every Frame
while run:
    Clock.tick(fps)
    screen.fill(background_color)
    
    # Set polygon properties
    new_position = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
    new_velocity = [random.randint(0, 2), -2]
    new_radius = random.randint(20, 40)
    new_poly_count = random.randint(3, 10)
    new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    new_life_time = 2

    new_polygon = Polygon(new_position, new_velocity, new_radius, new_poly_count, new_color, new_life_time)
    polygon_array.append(new_polygon)

    for polygon in polygon_array:
        polygon.draw_polygon()
        polygon.update_polygon()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
