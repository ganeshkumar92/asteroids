import pygame
import circleshape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOT_SPEED
from constants import PLAYER_SHOT_COOLDOWN
from shot import Shot

# Player class
class Player(circleshape.CircleShape):
    def __init__ (self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "White", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) # negative to rotate left
        if keys[pygame.K_d]:
            self.rotate(dt) # positive to rotate right
        if keys[pygame.K_w]:
            self.move(dt) # positive to move forward
        if keys[pygame.K_s]:
            self.move(-dt) # negative to move backward
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.shot_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * dt * PLAYER_SPEED

    def shoot(self):
        if self.shot_timer <= 0:      
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.shot_timer = PLAYER_SHOT_COOLDOWN
