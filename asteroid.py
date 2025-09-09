import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, WHITE, center, self.radius,  2)
        super().draw(screen)

    def update(self, dt):
        self.position += self.velocity * dt