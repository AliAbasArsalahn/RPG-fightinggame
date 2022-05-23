"""This module uses the pygame library to run the game"""


import pygame


WIDTH, HEIGHT = 1400, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG-fightinggame")

WHITE = (255, 255, 255)
RANDOM_COLOR = (140, 25, 55)

FPS = 60


def draw_window() -> None:
    """Set's display color to white"""
    WIN.fill(WHITE)
    WIN.blit()
    pygame.display.update()


def main() -> None:
    """main loop. Opens a window"""
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
