import pygame
import circleshape

from constants import SHOT_RADIUS

# Shot class

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt