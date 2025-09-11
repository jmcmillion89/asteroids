import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, WHITE, center, self.radius,  2)
        super().draw(screen)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        random_angle = random.uniform(20, 50)
        rotate = pygame.math.Vector2.rotate
        if (self.radius <= ASTEROID_MIN_RADIUS):
            self.kill()
            return
        self.kill()
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid1.velocity = rotate(self.velocity, random_angle) * 1.2
        new_asteroid2.velocity = rotate(self.velocity, -random_angle) * 1.2