import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rng = random.uniform(20, 50)
            velo1 = self.velocity.rotate(rng) * 1.2
            velo2 = self.velocity.rotate(-rng)* 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, new_radius).velocity = velo1
            Asteroid(self.position.x, self.position.y, new_radius).velocity = velo2
