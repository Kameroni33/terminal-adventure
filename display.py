
import os
import numpy as np

from enums import Pixel
import constants


class Display:
    check_active_pos = 0

    def __init__(self):
        self.screen = np.full(constants.SCREEN_SIZE, Pixel.NONE.value)
        self.set_border()
        self.set_character()

    def set_border(self):
        for i in range(constants.SCREEN_SIZE[0]):
            self.screen[i, 0] = Pixel.BORDER.value
            self.screen[i, -1] = Pixel.BORDER.value
        for i in range(constants.SCREEN_SIZE[1]):
            self.screen[0, i] = Pixel.BORDER.value
            self.screen[-1, i] = Pixel.BORDER.value

    def set_character(self):
        x_pos = int(constants.SCREEN_SIZE[0]/2)
        y_pos = int(constants.SCREEN_SIZE[1]/2)
        self.screen[x_pos, y_pos] = Pixel.CHARACTER.value

    def set_pixel(self, pos: tuple, pixel: Pixel):
        self.screen[pos[0], pos[1]] = pixel.value

    def print_screen(self):
        # Convert screen matrix into string format
        screen_string = ''
        for row in self.screen:
            for pixel in row:
                screen_string += pixel
            screen_string += '\n'
        # Print the string formatted screen
        os.system('cls')
        print(screen_string)

    def check_active(self):
        self.set_pixel((0, self.check_active_pos), Pixel.BORDER)
        if self.check_active_pos < constants.SCREEN_SIZE[1]-1:
            self.check_active_pos += 1
        else:
            self.check_active_pos = 0
        self.set_pixel((0, self.check_active_pos), Pixel.NONE)
