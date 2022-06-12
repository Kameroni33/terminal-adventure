
import keyboard

from enums import Key, Direction


class Controller:
    up_pressed = False
    down_pressed = False
    left_pressed = False
    right_pressed = False

    def __init__(self, new_elements):
        self.elements = new_elements

    def poll(self):
        if keyboard.is_pressed(Key.ESC.value):
            exit()
        if keyboard.is_pressed(Key.UP.value):
            self.up_pressed = True
            self.elements.move_character(Direction.NORTH)
        else:
            self.up_pressed = False
        if keyboard.is_pressed(Key.DOWN.value):
            self.down_pressed = True
            self.elements.move_character(Direction.SOUTH)
        else:
            self.down_pressed = False
        if keyboard.is_pressed(Key.LEFT.value):
            self.left_pressed = True
            self.elements.move_character(Direction.WEST)
        else:
            self.left_pressed = False
        if keyboard.is_pressed(Key.RIGHT.value):
            self.right_pressed = True
            self.elements.move_character(Direction.EAST)
        else:
            self.right_pressed = False
