
from enums import Direction, Pixel
import constants


class Elements:
    character_pos = [0, 0]
    enemy_pos = [0, 0]

    def __init__(self, new_display):
        self.display = new_display
        # Initialize Starting Objects
        self.initialize_character()
        self.initialize_enemy()

    def initialize_character(self):
        self.character_pos = [int(constants.SCREEN_SIZE[0] / 2), int(constants.SCREEN_SIZE[1] / 2)]
        self.display.set_pixel(self.character_pos, Pixel.CHARACTER)

    def initialize_enemy(self):
        self.enemy_pos = [3, 6]
        self.display.set_pixel(self.enemy_pos, Pixel.ENEMY)

    def move_character(self, direction: Direction):
        self.display.set_pixel(self.character_pos, Pixel.NONE)
        if direction == Direction.NORTH.value:
            if self.character_pos[0] > 1:
                self.character_pos[0] -= 1
        elif direction == Direction.SOUTH.value:
            if self.character_pos[0] < constants.SCREEN_SIZE[0] - 2:
                self.character_pos[0] += 1
        elif direction == Direction.EAST.value:
            if self.character_pos[1] < constants.SCREEN_SIZE[1] - 2:
                self.character_pos[1] += 1
        elif direction == Direction.WEST.value:
            if self.character_pos[1] > 2:
                self.character_pos[1] -= 1
        self.display.set_pixel(self.character_pos, Pixel.CHARACTER)

