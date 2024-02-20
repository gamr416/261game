import pygame
import sys
import os
from map import Map
from game import Game



MAPS_DIR = 'maps'
pygame.init()
SIZE = WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode(SIZE)
TILE_SIZE = 45
FPS = 30


def load_image(name, colorkey=None):
    # если файл не существует, то выходим
    if not os.path.isfile(name):
        print(f"Файл с изображением '{name}' не найден")
        sys.exit()
    image = pygame.image.load(name)
    return image


if __name__ == '__main__':
    MAP = Map([], [], [], 1)
    GAME = Game(map, 1)
    SCREEN.fill((0, 0, 255))
    pygame.display.set_caption('8a 261 gameplay')
    pygame.quit()