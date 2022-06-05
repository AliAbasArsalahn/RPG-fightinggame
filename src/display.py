"""display.py module"""

import pygame


class Display():
    """Display class; inherits from pygame.display"""

    def __init__(self, height: int, width: int, title: str) -> None:
        self.height = height
        self.width = width
        self.title = title
        self.COLOURS = {
            "white": (255, 255, 255)
        }

    def draw_window(self) -> None:
        pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
