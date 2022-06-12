
import time

import controller
import display
import elements
import constants


def run():
    display.print_screen()
    display.check_active()
    controller.poll()
    time.sleep(constants.REFRESH_RATE)


if __name__ == '__main__':
    display = display.Display()
    elements = elements.Elements(display)
    controller = controller.Controller(elements)
    # Main game loop
    while True:
        run()
