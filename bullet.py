import pygame
from settings import *

class Bullet:
    def __init__(self):
        self.image = pygame.image.load("assent/bala.png")
        self.x = 0
        self.y = 500
        self.speed = 20
        self.active = False

    def shoot(self, x):
        if not self.active:
            self.x = x
            self.active = True

    def move(self):
        if self.active:
            self.y -= self.speed
            if self.y < 0:
                self.active = False
                self.y = 500

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x + 16, self.y + 10))