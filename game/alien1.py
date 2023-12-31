import pygame
import random
from game import player
from game_parameters import *

class Alien1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('../g.assets/sprites/alien1.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(ALIEN1a, ALIEN1b)
        self.rect.center = (x,y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, space):
        space.blit(self.image, self.rect) #(self.rect.x, self.rect.y))



aliens1 = pygame.sprite.Group()

