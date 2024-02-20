import pygame
from map import Map


SIZE = WIDTH, HEIGHT = 1200, 600
SCREEN = pygame.display.set_mode(SIZE)

class Game:
    def __init__(self, map, gosha):
        self.map = map
        self.gosha = gosha

    def render(self, screen):
        self.map.render(screen)
