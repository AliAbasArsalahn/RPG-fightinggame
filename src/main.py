"""main.py module"""

import pygame
from display import Display


def main() -> None:
    """main loop. Opens a window"""
    pygame.init()
    display = Display(900, 1400, "RPG-fightinggame", 60)
    display.draw_window()
    display.window()


if __name__ == '__main__':
    main()
