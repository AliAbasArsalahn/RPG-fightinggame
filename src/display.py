"""display.py module"""

import pygame
from sys import exit


class Display():
    """Display class; inherits from pygame.display"""

    def __init__(self, height: int, width: int, title: str, fps: int) -> None:
        """Display constructor"""
        self.height = height
        self.width = width
        self.title = title
        self.WIN = pygame.display.set_mode((self.width, self.height))
        self.surface = pygame.Surface((self.width, self.height))
        self.FPS = fps
        self.clock = pygame.time.Clock()

    def draw_window(self) -> None:
        pygame.display.set_caption(self.title)
        self.WIN.blit(self.surface, (0, 0))
        pygame.display.update()

    def window(self) -> None:
        """opens a window. Window get's opened with set framerate from self.clock"""
        run = True
        while run:
            self.draw_window()
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    exit()

            self.draw_window()

        pygame.quit()
