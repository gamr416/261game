import pytmx

MAPS_DIR = 'maps'


class Map:
    def __init__(self, solid_tiles, collectables, finish_tiles, level):
        self.map = pytmx.util_pygame.load_pygame(f'{MAPS_DIR}/map{level}.tmx')
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = 45
        self.solid_tiles = solid_tiles
        self.finish_tiles = finish_tiles
        self.level = level

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                screen.blit(image, (x * self.tile_size, y * self.tile_size))

    def get_tile_id(self, position) -> int:
        return self.map.tiledgidmap.get(self.map.get_tile_gid(*position, 0))

    def is_free(self, position) -> bool:
        return self.get_tile_id(position) not in self.solid_tiles