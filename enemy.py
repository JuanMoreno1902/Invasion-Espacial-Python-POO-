import pygame
import random
from settings import *

class Enemy:
    def __init__(self):
        self.image = pygame.image.load("assent/enemigo.png")

        self.speed_x = ENEMY_SPEED
        self.speed_y = ENEMY_DROP_DISTANCE

        self.reset_position()

    def reset_position(self):
        self.x = random.randint(0, WIDTH - self.image.get_width())
        self.y = random.randint(50, 200)

    def move(self):
        self.x += self.speed_x

        # Rebotar en bordes
        if self.x <= 0 or self.x >= WIDTH - self.image.get_width():
            self.speed_x *= -1
            self.y += self.speed_y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))