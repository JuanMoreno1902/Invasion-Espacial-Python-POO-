import pygame
from settings import *

class Player:
    def __init__(self):
        self.image = pygame.image.load("assent/astronave.png")
        self.x = 368
        self.y = 520
        self.speed = 5

    def move(self, direction):
        self.x += direction * self.speed
        self.x = max(0, min(736, self.x))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))