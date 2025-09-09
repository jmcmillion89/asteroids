import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, WHITE, center, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt